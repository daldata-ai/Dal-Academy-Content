# Contributing to Dal Academy Content

This guide is for TAs and other contributors. Students read this content directly on GitHub, so everything merged into `main` is live for them as soon as it merges.

## Workflow

1. **Get the latest `main`:** `git checkout main && git pull`
2. **Create a branch** using the naming rule below.
3. **Make your changes** following the conventions in this guide.
4. **Run the checks locally** with `python scripts/check_content.py`.
5. **Open a pull request** and fill in the template. One reviewer approval is enough to merge. For typo fixes, any TA can approve.
6. **Squash and merge** when the checks pass and the PR is approved.

### Branch names

| Change | Branch | Example |
|--------|--------|---------|
| New module or section | `content/<module>-<topic>` | `content/03-data-modeling` |
| Fix an error or typo | `fix/<module>-<short-desc>` | `fix/02-window-example` |
| Repo setup, templates, scripts | `chore/<short-desc>` | `chore/update-requirements` |

Keep PRs small and limited to one module where possible, because notebook diffs are hard to review.

## Repository structure

Each module lives in its own folder named `NN-kebab-case-name`:

```
modules/03-data-modeling/
  README.md                  # required: overview, objectives, prerequisites
  03-data-modeling.ipynb     # required: main notebook, same name as the folder
  assets/                    # optional: images used in the notebook
  data/                      # optional: small datasets (< 5 MB each)
  resources/                 # optional: slides, PDFs, cheat sheets
  exercises/                 # optional: extra practice notebooks
```

To start a new module, copy `modules/_template/`, rename the folder and the notebook, and add a row to the module table in the root [README.md](README.md).

## Notebook conventions

All notebooks follow the same structure, as in modules 01 and 02:

1. **Cover cell:** Dal-branded header with the kicker (`NOTEBOOK NN / 06`), title, subtitle and topic chips. Copy it from the template.
2. **"What you will be able to do":** 4–6 measurable objectives, plus level, working style and dataset.
3. **Environment cell:** imports, the Dal plotting palette, and `SEED = 42`.
4. **Numbered sections** (`## 1. …`) following the pattern *concept → demonstration → production note*.
5. **Lab:** a hands-on task for students.
6. **Checkpoint:** 4–6 review questions.
7. **References & further reading:** prefer official documentation, followed by the Dal footer.

### Before committing a notebook

- **Restart the kernel and run all cells.** Cells must run top to bottom without errors, and outputs must be in order.
- **Keep the outputs.** Students browse on GitHub, so charts and tables need to be visible without running anything.
- **Generate data inside the notebook** with a fixed seed where possible. If you need a file, put it in the module's `data/` folder and load it with a relative path.
- **Remove secrets, personal paths, and leftover debug cells.**
- Use only libraries listed in [requirements.txt](requirements.txt). If you need a new one, add it in the same PR and explain why.

## Writing style

- **Language:** English. Write in clear, direct sentences for learners at foundation to intermediate level.
- **Terms:** define each technical term the first time it appears, and use it consistently after that.
- **Headings:** use `##` for numbered sections and `###` for subsections. Use sentence case.
- **Code:** add short comments that explain *why*, not *what*. Keep variable names meaningful.
- **Callouts:** use `>` blockquotes for production notes and warnings.
- **Links:** use relative links within the repo, and full URLs for external sources.
- **Images:** save them in the module's `assets/` folder and give each one alt text.

## Files and sizes

- Keep individual files under **20 MB**; the automated check rejects larger ones. Link to large datasets externally instead.
- Prefer formats that diff well, such as Markdown and CSV, over binary formats where you have the choice.
- Name files in lowercase kebab-case with no spaces, for example `window-types.png`.

## Automated checks

Every PR runs [scripts/check_content.py](scripts/check_content.py), which checks:

- notebooks are valid JSON and contain no error outputs
- each module folder has a `README.md` and a notebook named after the folder
- relative links in Markdown files point to files that exist
- no file is larger than 20 MB

Run the same checks locally with `python scripts/check_content.py`.

## Solutions

Do not commit exercise or lab solutions to this repository, because students can see everything in it.
