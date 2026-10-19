"""Lightweight content checks for Dal Academy. Run: python scripts/check_content.py

Uses only the standard library, so it runs without installing anything.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "modules"
MAX_FILE_MB = 20
MODULE_NAME = re.compile(r"^\d{2}-[a-z0-9]+(-[a-z0-9]+)*$")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", ".venv", "venv", "env", ".ipynb_checkpoints", "__pycache__"}

errors = []


def rel(path):
    return path.relative_to(ROOT).as_posix()


def tracked_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and not SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            yield path


def check_file_sizes():
    for path in tracked_files():
        size_mb = path.stat().st_size / 1_000_000
        if size_mb > MAX_FILE_MB:
            errors.append(f"{rel(path)}: {size_mb:.1f} MB exceeds {MAX_FILE_MB} MB limit")


def check_modules():
    for folder in sorted(p for p in MODULES.iterdir() if p.is_dir()):
        if folder.name == "_template":
            continue
        if not MODULE_NAME.match(folder.name):
            errors.append(f"{rel(folder)}: folder name must look like 03-data-modeling")
        if not (folder / "README.md").exists():
            errors.append(f"{rel(folder)}: missing README.md")
        if not (folder / f"{folder.name}.ipynb").exists():
            errors.append(f"{rel(folder)}: missing main notebook {folder.name}.ipynb")


def check_notebooks():
    for path in tracked_files():
        if path.suffix != ".ipynb":
            continue
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel(path)}: invalid notebook JSON ({exc})")
            continue
        for i, cell in enumerate(nb.get("cells", []), start=1):
            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    name = output.get("ename", "Error")
                    errors.append(f"{rel(path)}: cell {i} has an error output ({name}); rerun the notebook")


def check_links():
    for path in tracked_files():
        if path.suffix != ".md":
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in MD_LINK.findall(text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            target_path = target.split("#")[0]
            if target_path.startswith("../../issues"):  # GitHub web route, not a file
                continue
            if target_path and not (path.parent / target_path).exists():
                errors.append(f"{rel(path)}: broken link -> {target}")


if __name__ == "__main__":
    check_file_sizes()
    check_modules()
    check_notebooks()
    check_links()
    if errors:
        print(f"{len(errors)} problem(s) found:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    print("All content checks passed.")
