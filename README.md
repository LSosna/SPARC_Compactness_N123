# SPARC Gravitational Compactness Project
**Version:** 2.1 (Final Submission Release)
**Date:** December 2025

# SPARC Compactness Canonical Dataset (N=123)

[![DOI](https://zenodo.org/badge/1125461184.svg)](https://doi.org/10.5281/zenodo.18099710)

Canonical N=123 SPARC compactness dataset, code, and verification files for the paper
*“Gravitational Compactness of SPARC Disk Galaxies.”*

- **GitHub Release:** [v1.0](https://github.com/LSosna/SPARC_Compactness_N123/releases/tag/v1.0)
- **Permanent DOI:** [10.5281/zenodo.18099710](https://doi.org/10.5281/zenodo.18099710)
- **License:** CC-BY 4.0 (for data) and MIT (for code)

## 1. Overview
This repository contains the complete data, code, and statistical evidence for the manuscript:
**"Gravitational Compactness of SPARC Disk Galaxies: A Quantitative Benchmark for Angular Momentum Conservation"**

The analysis establishes the "Disk Stability Floor" at $\lambda \approx 10^{-7.1}$ and performs a Bayesian Model Comparison (BIC) rejecting global-lambda dynamics in favor of the Radial Acceleration Relation (RAR).

---

## 2. File Manifest

### Primary Data
* **`SPARC_Canonical123.csv`**: The "Single Source of Truth" dataset. Contains properties for the strict sample of **N=123** galaxies (Quality ≤ 3, 30° < i < 80°).
    * _Columns:_ `Name`, `Dist_Mpc`, `M_bar` (Baryonic Mass), `R_eff` (Effective Radius), `lambda` (Compactness), `log_lambda`, `slope_s` inputs.

### Statistical Verification
* **`canonical_FINAL_CORRECTED.json`**: Machine-readable summary of all derived values (Slopes $s$ and $\alpha$, Scatter $\sigma$, $\Delta$BIC). All manuscript numbers are pulled from here.
* **`BIC_Verification_summary.json`**: Detailed output of the Bayesian Information Criterion test, comparing the Standard RAR vs. Global $\lambda$-Scaling models.

### Reproducibility Code
* **`“sparc_canonical_final.py`**: A standalone Python script.
    * **Function:** Ingests raw SPARC data, applies cuts, performs ODR fitting, and generates the figures.
    * **Usage:** Can be run locally or in Google Colab.

---

## 3. How to Reproduce Results

### System Requirements
* Python 3.8+
* Libraries: `numpy`, `scipy`, `pandas`, `matplotlib`

### Instructions
1. Place `generate_canonical.py` in the same folder as the raw SPARC data (or point it to the VizieR URL).
2. Run the script:
   ```bash
   python generate_canonical.py

## 4. Verification and Checksums
Each major file has been validated against its canonical results.

| File | SHA-256 | Notes |
|------|----------|-------|
| SPARC_Canonical123.csv | [insert hash] | N=123 canonical dataset |
| canonical_FINAL_CORRECTED.json | [insert hash] | Machine-readable summary |
| BIC_Verification_summary.json | [insert hash] | Model comparison output |
| generate_canonical.py | [insert hash] | Reproducibility script |
| SPARC_Manuscript_N123_FINAL.docx | [insert hash] | Published manuscript text |

All hashes were generated using `sha256sum` to ensure integrity during upload and review.

## 5. Citation
@dataset{sosna_sparc_2025,
  author    = {Sosna, Lukas},
  title     = {SPARC Gravitational Compactness Dataset (N=123)},
  year      = {2025},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18099710},
  url       = {https://doi.org/10.5281/zenodo.18099710}## Version History
- **v1.1 (2025-12-30)** — UTF-8 corrected release (current)
- **v1.0 (2025-12-28)** — initial release with binary/RTF files
- Sosna, L. (2025). SPARC Compactness N = 123: Canonical Dataset (v1.1). Zenodo. https://doi.org/10.5281/zenodo.18100150
}
