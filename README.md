# SPARC Gravitational Compactness: Data & Code Archive

**Version:** 2.3 (Final Submission)  
**Date:** January 2026  
**Paper Title:** *Gravitational Compactness of SPARC Galaxies: Structural Constraints and Decisive Falsification of Global Dynamical Scaling*

---

## 1. Overview

This repository contains the canonical dataset, analysis scripts, and statistical verification logs for the associated manuscript. The analysis establishes the structural "Disk Stability Floor" at λ ≈ 10⁻⁷·¹ and performs a Bayesian Model Comparison that **decisively falsifies** global-λ dynamics (ΔBIC ≈ 2.6 × 10⁵).

### Key Results

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| **ΔBIC** | +2.64 × 10⁵ | Decisive falsification of global-λ dynamics |
| **Compactness Slope** | s = 0.742 ± 0.020 | λ ∝ M^0.74 scaling |
| **Intrinsic Scatter** | σ = 0.22 dex | Cosmic variance (not observational noise) |
| **Baryon Retention** | η ≈ 0.23 | f_b ∝ M^0.23 constraint |
| **Median λ** | 7.2 × 10⁻⁸ | Characteristic disk compactness |

---

## 2. File Manifest

### A. Primary Data

| File | Description |
|------|-------------|
| `SPARC_Canonical123.csv` | Canonical N=123 dataset with all galaxy properties |
| `canonical_FINAL_CORRECTED.json` | Machine-readable summary of fit parameters |

### B. Analysis Code

| File | Description |
|------|-------------|
| `SPARC_canonical_rebuild_v2.3.py` | Main analysis script (ODR fits, BIC calculation, figures) |

### C. Verification Logs

| File | Description |
|------|-------------|
| `BIC_Verification_summary.json` | Detailed BIC model comparison output |
| `CHECKSUMS.txt` | SHA-256 hashes for file integrity |

---

## 3. Reproduction Instructions

### System Requirements
- Python 3.8+
- Libraries: `numpy`, `pandas`, `scipy`, `matplotlib`

### Steps

1. **Clone or download** this repository
2. **Place data files** in the working directory
3. **Run the analysis:**
   ```bash
   python SPARC_canonical_rebuild_v2.3.py
   ```
4. **Outputs generated:**
   - Figure 1: Compactness vs Baryonic Mass
   - Figure 2: Effective Radius vs Baryonic Mass
   - Figure 3: Distribution of log₁₀λ
   - Figure 4: BIC Model Comparison
   - Console verification of all canonical values

---

## 4. Canonical Values

### Structural Parameters
```
N = 123 galaxies
Median λ = 7.2 × 10⁻⁸ (log₁₀λ = -7.14)
95% CI: [5.6, 9.9] × 10⁻⁸

Compactness slope: s = 0.742 ± 0.020
Direct size slope: α = 0.296 ± 0.020
Inferred size slope: α_infer = 0.258 ± 0.020

Intrinsic scatter: σ = 0.22 dex
  - Inclination correlation: r = 0.055, p = 0.55
  - Gas fraction correlation: r = 0.027, p = 0.77
```

### Dynamical Falsification
```
n = 2,725 rotation-curve points
σ_floor = 2 km/s

BIC(RAR) = 1.44 × 10⁵
BIC(λ) = 4.08 × 10⁵
ΔBIC = +2.64 × 10⁵ (RAR decisively preferred)

Best-fit γ ≈ -4 × 10⁻⁴ ≈ 0 (no λ dependence)
```

### Baryon Retention Constraint
```
From compactness: η ≈ 0.23 (primary)
From direct fit: η ≈ 0.11 (consistency check)
Adopted range: η ≈ 0.1–0.3
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
G = 6.67430 × 10⁻¹¹ m³ kg⁻¹ s⁻²
c = 2.99792458 × 10⁸ m s⁻¹
M_sun = 1.98847 × 10³⁰ kg
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
  doi       = {10.5281/zenodo.18099710}
}
```

---

## 8. License

- **Data:** CC-BY 4.0
- **Code:** MIT License

---

## 9. Contact

For questions about this dataset or analysis, please open an issue on the GitHub repository or contact the author.
