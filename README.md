<p align="center">
  <img src="assets/banner.svg" alt="Dal Academy · Data & AI Learning Series" width="100%">
</p>

<p align="center">
  <a href="#modules"><img src="https://img.shields.io/badge/modules-2_of_6-B91C4B?style=flat-square" alt="Modules: 2 of 6"></a>
  <img src="https://img.shields.io/badge/python-3.9%2B-7A0F31?style=flat-square&logo=python&logoColor=white" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/level-foundation_→_intermediate-4D091E?style=flat-square" alt="Level: foundation to intermediate">
  <a href="https://daldata.ai"><img src="https://img.shields.io/badge/daldata.ai-visit-B91C4B?style=flat-square" alt="daldata.ai"></a>
</p>

<p align="center">
  <b>Hands-on notebooks that take you from raw data to production-grade data systems.</b><br>
  Every module pairs clear concepts with runnable code, real production notes, a lab, and a checkpoint.
</p>

<p align="center">
  <a href="#modules">Modules</a> ·
  <a href="#get-started">Get started</a> ·
  <a href="#how-each-module-works">How modules work</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

---

## Modules

| | Module | What you'll learn | Level | Open |
|:-:|---|---|---|:-:|
| **01** | [**Data Foundations & Data Types**](modules/01-data-foundations/) | Data forms, dtypes vs business meaning, profiling, data quality, schema evolution, data contracts | Foundation | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hanoufalmogri/Dal-Academy-Content/blob/main/modules/01-data-foundations/01-data-foundations.ipynb) |
| **02** | [**Data Processing Architectures**](modules/02-processing-architectures/) | Batch, micro-batch, streaming, event time, windows, state, idempotency, backpressure | Intermediate | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hanoufalmogri/Dal-Academy-Content/blob/main/modules/02-processing-architectures/02-processing-architectures.ipynb) |
| **03** | _Coming soon_ | | | |
| **04** | _Coming soon_ | | | |
| **05** | _Coming soon_ | | | |
| **06** | _Coming soon_ | | | |

### Learning path

```mermaid
flowchart LR
    M1["01 · Data Foundations"] --> M2["02 · Processing Architectures"] --> M3["03 · Coming soon"] --> M4["04 · Coming soon"] --> M5["05 · Coming soon"] --> M6["06 · Coming soon"]
    classDef live fill:#B91C4B,stroke:#7A0F31,color:#FFFFFF,font-weight:bold
    classDef soon fill:#F8E9EE,stroke:#E8D9DE,color:#6F6268
    class M1,M2 live
    class M3,M4,M5,M6 soon
```

## Get started

**Fastest way:** click **Open in Colab** next to any module. It runs in your browser with nothing to install.

<details>
<summary><b>Prefer to run locally?</b></summary>

<br>

You'll need Python 3.9 or newer.

```bash
git clone https://github.com/hanoufalmogri/Dal-Academy-Content.git
cd Dal-Academy-Content
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

All datasets are generated inside the notebooks, so nothing needs to be downloaded.

</details>

## How each module works

Every notebook follows the same rhythm, so you always know where you are:

| Step | What happens |
|---|---|
| 🎯 **Objectives** | What you'll be able to do by the end |
| 💡 **Concept** | The idea in plain language, with terms defined |
| 🧪 **Demonstration** | Runnable code on reproducible data |
| 🏭 **Production note** | How it shows up in real systems, and the common mistakes |
| 🛠️ **Lab** | A hands-on task you build yourself |
| ✅ **Checkpoint** | Questions to confirm you've got it |

## Questions or found a mistake?

[Open an issue](https://github.com/hanoufalmogri/Dal-Academy-Content/issues/new/choose) and pick **Content error** or **Question**. Include the module number and section.

---

<p align="center">
  <sub><b>DAL | دال</b> · Guiding a generation of data leaders · <a href="https://daldata.ai">daldata.ai</a></sub>
</p>
