# SPARC Compactness Canonical Analysis (v3.0)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18100150.svg)](https://doi.org/10.5281/zenodo.18100150)

Canonical SPARC Compactness dataset (N = 123 galaxies), providing the gravitational
compactness scaling λ ≡ GM_bar / (R_eff c²), with power-law slope s = 0.742 ± 0.020.

---

### 📊 Key Results
| Parameter | Value | Description |
|------------|--------|-------------|
| N | 123 | Canonical sample size |
| s | 0.742 ± 0.020 | Compactness slope |
| α_direct | 0.296 ± 0.020 | Direct R–M fit |
| α_inferred | 0.258 | From 1 − s |
| η_primary | 0.22–0.23 | Baryon retention scaling |
| σ | 0.21 dex | Intrinsic scatter |
| ΔBIC | 2.6×10⁵ | RAR strongly favored over λ-model |

---

### 📁 File Manifest
| File | Description |
|------|--------------|
| `SPARC_Canonical123.csv` | Canonical dataset (N=123) |
| `canonical_FINAL_CORRECTED.json` | Derived canonical quantities |
| `BIC_Verification_summary.json` | Bayesian comparison summary |
| `SPARC_canonical_rebuild_v3.0.py` | Reproducible rebuild script |
| `Sparc_canonical_final.py` | Legacy analysis script |
| `CHECKSUMS.txt` | SHA256 verification file |
| `SPARC_Manuscript_FINAL_v3.md` | Markdown manuscript |
| `SPARC_Manuscript_FINAL_FORMATTED.docx` | Submission-ready Word file |
| `Figures/` | Publication figures 1–4 |

---

### 🔁 Reproduction
To rebuild the canonical archive:

```bash
!python SPARC_canonical_rebuild_v3.0.py
