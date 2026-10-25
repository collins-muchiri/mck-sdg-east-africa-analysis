# mck-sdg-east-africa-analysis

*Portfolio artifact 1 — applied statistical analysis of public UN SDG data for East Africa; Python.*

![category](https://img.shields.io/badge/category-data-science-0EA5E9?style=flat-square) ![language](https://img.shields.io/badge/language-Python-2563EB?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-16A34A?style=flat-square) ![maintenance](https://img.shields.io/badge/maintenance-active-16A34A?style=flat-square) ![repo](https://img.shields.io/badge/repo-mck--sdg--east--africa--analysis-111827?style=flat-square)

---

Applied statistical analysis of public United Nations SDG data for East Africa. Portfolio artifact 1.

## What this repository now contains

weeks/week01 to weeks/week06: six reproducible modules, one per concept of the statistical
inference sequence, each with an analysis script, a results note and a figure. week01 samples and
bias; week02 intervals; week03 confounding; week04 regression diagnostics; week05 power and minimum
detectable effect; week06 difference-in-differences with a disclosed failed pre-trend.
docs/ARTIFACT1_BRIEF.pdf: the two-page brief written for a programme director.
docs/ and MODEL_CARD.md, DATA_PROVENANCE.md, docs/DPIA.md: governance documents.

## Reproduce

    pip install -r requirements.txt
    python3 weeks/week01/week01_sampling_bias.py
    python3 weeks/week02/week02_analysis.py
    python3 weeks/week03/week03_analysis.py
    python3 weeks/week04/week04_analysis.py
    python3 weeks/week05/week05_analysis.py
    python3 weeks/week06/week06_analysis.py

Week01 needs network access and caches pages locally. All others run offline from the committed CSV.

## Reading order for a reviewer

docs/ARTIFACT1_BRIEF.pdf first, then weeks/week01/week01_results.md, then whichever week matches the
claim you are checking. Every results note ends with its limitations, written before the numbers
were known to be flattering.

## Status and honesty notes

Data provenance sidecars carry TO VERIFY fields until the account holder fills them from download
records; train_model.py refuses to run until they are filled, by design. Model metrics are not
published until that gate clears. No synthetic data is present in this repository; the synthetic
work lives in mck-dashboard-to-insight and is labelled there.

## Licence

MIT.

## Contribution and license

Issues and pull requests are welcome — please open an issue describing the proposed change before submitting substantive work. This project is released under the MIT License.
