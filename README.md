# SPARC Compactness Canonical Dataset (v3.1)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18100150.svg)](https://doi.org/10.5281/zenodo.18100150)

Canonical N=123 SPARC compactness dataset and reproducibility package accompanying:

**Sosna (2026)** — *“Gravitational Compactness of SPARC Galaxies: A Three-Parameter Benchmark for Baryon Retention and Decisive Falsification of Global Dynamical Scaling.”*

---
# SPARC Gravitational Compactness: Data & Code Archive

**Version:** 3.1 (Final Submission)  
**Date:** January 2026  
**Paper Title:** *Gravitational Compactness of SPARC Galaxies: Structural Constraints and Decisive Falsification of Global Dynamical Scaling*


### 📊 Key Results

| Parameter | Value | Description |
|------------|--------|-------------|
| N | 123 | Canonical SPARC galaxy sample |
| s | 0.742 ± 0.020 | Compactness slope |
| α_direct | 0.296 ± 0.020 | Direct R–M fit |
| α_inferred | 0.258 | From 1 − s |
| η_primary | 0.10–0.23 | Baryon retention scaling zone |
| σ | 0.21 dex | Intrinsic scatter (ΛCDM variance ceiling) |
| ΔBIC | +2.6×10⁵ | RAR strongly favored over λ-model |

---

### 📁 Included Files

| File | Description |
|------|--------------|
| `SPARC_Canonical123.csv` | Canonical dataset (N=123) |
| `canonical_FINAL_v3.1.json` | Canonical compactness and scaling parameters |
| `BIC_Verification_summary.json` | Bayesian model comparison results |
| `SPARC_canonical_rebuild_v3.1.py` | Reproducible rebuild script |
| `CHECKSUMS.txt` | Integrity verification manifest |
| `Empirical_Compactness_Scaling_in_Disk_Galaxies_SUBMISSION_FINAL.pdf` | Final manuscript |
| `README.md` | Documentation and summary (this file) |

---

### 🔁 Reproduction

To rebuild the canonical compactness dataset locally:

```bash
python SPARC_canonical_rebuild_v3.1.py

---

## 1. Overview

This repository contains the canonical dataset, analysis scripts, and statistical verification logs for the associated manuscript. The analysis establishes gravitational compactness λ as a **tight structural organizer** (s = 0.742 ± 0.020) while delivering **categorical closure** on global-λ dynamics (ΔBIC ≈ +2.6 × 10⁵).

### Key Results

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| **ΔBIC** | +2.64 × 10⁵ | Categorical closure on global-λ dynamics |
| **Compactness Slope** | s = 0.742 ± 0.020 | λ ∝ M^0.74 scaling |
| **Intrinsic Scatter** | σ = 0.21 dex | Boundary condition on ΛCDM stochasticity |
| **Baryon Retention** | η ≈ 0.1–0.23 | Unified simulation target zone |
| **Median λ** | 7.3 × 10⁻⁸ | Characteristic disk compactness |

---

## 2. File Manifest

### A. Primary Data

| File | Description |
|------|-------------|
| `SPARC_Canonical123.csv` | Canonical N=123 dataset with all galaxy properties |
| `canonical_FINAL_v3.1.json` | Machine-readable summary of fit parameters |

### B. Analysis Code

| File | Description |
|------|-------------|
| `SPARC_canonical_rebuild_v3.1.py` | Main analysis script (ODR fits, scatter validation) |
| `Sparc_canonical_final.py` | Legacy verification script |

### C. Verification Logs

| File | Description |
|------|-------------|
| `BIC_Verification_summary.json` | Detailed BIC model comparison output |
| `CHECKSUMS.txt` | SHA-256 hashes for file integrity |

### D. Manuscript

| File | Description |
|------|-------------|
| `SPARC_Manuscript_FINAL_v3.1.md` | Markdown manuscript |
| `SPARC_Manuscript_FINAL_FORMATTED.docx` | Submission-ready Word file |

---

## 3. Reproduction Instructions

### System Requirements
- Python 3.8+
- Libraries: `numpy`, `pandas`, `scipy`

### Steps

1. **Clone or download** this repository
2. **Place data files** in the working directory
3. **Run the analysis:**
   ```bash
   python SPARC_canonical_rebuild_v3.1.py
   ```
4. **Outputs generated:**
   - `canonical_FINAL_v3.1.json` — canonical values
   - `BIC_Verification_summary.json` — model comparison
   - `CHECKSUMS.txt` — integrity verification

---

## 4. Canonical Values

### Structural Parameters
```
N = 123 galaxies
Median λ = 7.3 × 10⁻⁸ (log₁₀λ = -7.14)
95% CI: [5.6, 9.9] × 10⁻⁸

Compactness slope: s = 0.742 ± 0.020
Direct size slope: α = 0.296 ± 0.020
Inferred size slope: α_infer = 0.258 ± 0.020

Intrinsic scatter: σ = 0.21 dex
  - Inclination correlation: r = 0.055, p = 0.54
  - Gas fraction correlation: r = 0.025, p = 0.78
```

### Baryon Retention Target Zone
```
From compactness: η ≈ 0.23
From direct fit: η ≈ 0.11
Unified target zone: η ≈ 0.1–0.23
```

### Dynamical Falsification
```
n = 2,725 rotation-curve points
σ_floor = 2 km/s

BIC(RAR) = 1.44 × 10⁵
BIC(λ) = 4.08 × 10⁵
ΔBIC = +2.64 × 10⁵ (RAR decisively preferred)

Best-fit γ ≈ 0 (no λ dependence)
```

---

## 5. Sample Selection Criteria

Starting from SPARC (175 galaxies):
1. Quality cut: Q ≤ 3
2. Inclination cut: 30° < i < 80°
3. Valid R_eff and M_HI
4. Exclude 7 systems with photometric anomalies

**Final sample: N = 123 galaxies**

---

## 6. Physical Constants (CODATA-2018)

```
G = 6.6743 × 10⁻¹¹ m³ kg⁻¹ s⁻²
c = 2.99792458 × 10⁸ m s⁻¹
M_sun = 1.989 × 10³⁰ kg
kpc = 3.0857 × 10¹⁹ m
Υ_3.6 = 0.5 M_sun/L_sun
```

---

## 7. Citation

```bibtex
@article{sosna2026sparc,
  author  = {Sosna, Lukas},
  title   = {Gravitational Compactness of {SPARC} Galaxies: 
             Structural Constraints and Decisive Falsification 
             of Global Dynamical Scaling},
  journal = {Monthly Notices of the Royal Astronomical Society},
  year    = {2026},
  note    = {Submitted}
}

@dataset{sosna2026data,
  author    = {Sosna, Lukas},
  title     = {{SPARC} Gravitational Compactness Dataset (N=123)},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18100150}
}
```

---

## 8. License

- **Data:** CC-BY 4.0
- **Code:** MIT License

---

## 9. Changelog

### v3.1 (January 2026)
- Unified η as simulation target zone (0.1–0.23)
- Reframed scatter as ΛCDM boundary condition
- Corrected JSON canonical values
- Updated to Zenodo DOI

### v3.0 (January 2026)
- Narrative rebalancing per editorial feedback
- Falsification moved to headline position

### v2.x (December 2025)
- Initial canonical dataset and analysis

