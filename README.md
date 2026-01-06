# SPARC Compactness Canonical Dataset (v3.1)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18100150.svg)](https://doi.org/10.5281/zenodo.18100150)

Canonical N=123 SPARC compactness dataset and reproducibility package accompanying:

**Sosna (2026)** — *“Gravitational Compactness of SPARC Galaxies: A Three-Parameter Benchmark for Baryon Retention and Decisive Falsification of Global Dynamical Scaling.”*

---

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
