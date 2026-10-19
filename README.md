# Dal Academy · Data & AI Learning Series

Course content for Dal Academy students: hands-on Jupyter notebooks covering data foundations, processing architectures, and production data engineering.

> **Students:** start with [Getting started](#getting-started), then work through the modules in order.
> **TAs and contributors:** read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Modules

| # | Module | What you'll learn |
|---|--------|-------------------|
| 01 | [Data Foundations & Data Types](modules/01-data-foundations/) | Structured vs semi-structured vs unstructured data, dtypes, profiling, data quality, schema evolution, data contracts |
| 02 | [Data Processing Architectures](modules/02-processing-architectures/) | Batch, micro-batch, streaming, event time, windowing, state, idempotency, backpressure |
| 03 | _Coming soon_ | |
| 04 | _Coming soon_ | |
| 05 | _Coming soon_ | |
| 06 | _Coming soon_ | |

Each module folder has a `README.md` with its learning objectives and a notebook you can run.

## Getting started

You can read every notebook directly on GitHub: just click it. To run the code yourself, choose one of these options:

### Option A: Google Colab (no install)

Open a notebook on GitHub, then replace `github.com` in the URL with `githubtocolab.com`. Colab already includes everything these notebooks need.

### Option B: Run locally

You'll need Python 3.9 or newer.

```bash
git clone <this-repo-url>
cd Dal-Academy-Content
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

All datasets are generated inside the notebooks, so nothing needs to be downloaded.

## Repository layout

```
modules/
  01-data-foundations/
    README.md                     ← module overview & objectives
    01-data-foundations.ipynb     ← the main notebook
  02-processing-architectures/
  _template/                      ← starting point for new modules (contributors)
scripts/                          ← automated content checks
```

## Found a mistake or have a question?

[Open an issue](../../issues/new/choose) and pick **Content error** or **Question**. Include the module number and section.
