#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPARC Compactness Canonical Analysis — v3.1
============================================
Canonical analysis script for SPARC gravitational compactness.

Accompanies: "Gravitational Compactness of SPARC Galaxies: Structural 
Constraints and Decisive Falsification of Global Dynamical Scaling"

Author: Lukas Sosna
Date: January 2026
License: MIT
"""

import os
import json
import hashlib
import numpy as np
import pandas as pd
from scipy import stats
from scipy.odr import ODR, Model, RealData

# ============================================================
# CONFIGURATION
# ============================================================
DATA_PATH = "SPARC_Canonical123.csv"
OUTPUT_DIR = "SPARC_Publication_Archive_v3.1"

# Physical constants (CODATA-2018)
G = 6.6743e-11        # m³ kg⁻¹ s⁻²
c = 2.99792458e8      # m s⁻¹
M_sun = 1.989e30      # kg
kpc_to_m = 3.0857e19  # m

# SPARC conventions
UPSILON_3p6 = 0.5     # Stellar mass-to-light ratio (M☉/L☉)
HI_CORRECTION = 1.33  # Helium correction factor

# BIC values from rotation curve analysis (pre-computed)
BIC_RAR = 144173.4
BIC_LAMBDA = 407826.4
N_RC_POINTS = 2725
K_RAR = 1
K_LAMBDA = 2

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def linear_model(B, x):
    """Linear model for ODR: y = B[0]*x + B[1]"""
    return B[0] * x + B[1]

def sha256_file(filepath):
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(4096), b''):
            sha256.update(block)
    return sha256.hexdigest()

# ============================================================
# MAIN ANALYSIS
# ============================================================
def main():
    print("=" * 60)
    print("SPARC Compactness Canonical Analysis v3.1")
    print("=" * 60)
    
    # ----------------------------------------------------------
    # 1. Load Data
    # ----------------------------------------------------------
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")
    
    df = pd.read_csv(DATA_PATH)
    N = len(df)
    print(f"\n[1] Loaded {N} galaxies from {DATA_PATH}")
    
    # ----------------------------------------------------------
    # 2. Compute Baryonic Mass
    # ----------------------------------------------------------
    df["M_star"] = UPSILON_3p6 * df["L3.6_GLsun"] * 1e9  # M☉
    df["M_HI"] = df["MHI_GMsun"] * 1e9                    # M☉
    df["M_bar"] = df["M_star"] + HI_CORRECTION * df["M_HI"]
    
    print(f"[2] Baryonic mass range: {df['M_bar'].min():.2e} – {df['M_bar'].max():.2e} M☉")
    
    # ----------------------------------------------------------
    # 3. Compute Gravitational Compactness
    # ----------------------------------------------------------
    df["lambda"] = (G * df["M_bar"] * M_sun) / (df["Reff_kpc"] * kpc_to_m * c**2)
    df["log_lambda"] = np.log10(df["lambda"])
    df["log_Mb"] = np.log10(df["M_bar"])
    
    median_lambda = np.median(df["lambda"])
    log_median = np.median(df["log_lambda"])
    
    print(f"[3] Median λ = {median_lambda:.2e} (log₁₀λ = {log_median:.2f})")
    
    # ----------------------------------------------------------
    # 4. ODR Fit: λ–M_bar Scaling
    # ----------------------------------------------------------
    data_lambda = RealData(df["log_Mb"], df["log_lambda"])
    odr_lambda = ODR(data_lambda, Model(linear_model), beta0=[0.7, -14])
    result_lambda = odr_lambda.run()
    
    s = result_lambda.beta[0]
    s_err = result_lambda.sd_beta[0]
    intercept = result_lambda.beta[1]
    
    # Compute residuals and scatter
    df["predicted"] = s * df["log_Mb"] + intercept
    df["residual"] = df["log_lambda"] - df["predicted"]
    scatter_dex = df["residual"].std()
    
    print(f"[4] ODR Fit: s = {s:.3f} ± {s_err:.3f}")
    print(f"    Residual scatter σ = {scatter_dex:.3f} dex")
    
    # ----------------------------------------------------------
    # 5. ODR Fit: R_eff–M_bar Scaling
    # ----------------------------------------------------------
    data_radius = RealData(df["log_Mb"], np.log10(df["Reff_kpc"]))
    odr_radius = ODR(data_radius, Model(linear_model), beta0=[0.3, -3])
    result_radius = odr_radius.run()
    
    alpha_direct = result_radius.beta[0]
    alpha_direct_err = result_radius.sd_beta[0]
    
    print(f"[5] Direct fit: α_direct = {alpha_direct:.3f} ± {alpha_direct_err:.3f}")
    
    # ----------------------------------------------------------
    # 6. Derived Quantities
    # ----------------------------------------------------------
    alpha_infer = 1 - s
    eta_from_compactness = 1 - 3 * alpha_infer
    eta_from_direct = 1 - 3 * alpha_direct
    
    print(f"\n[6] Derived quantities:")
    print(f"    α_inferred = 1 - s = {alpha_infer:.3f}")
    print(f"    η (from compactness) = {eta_from_compactness:.2f}")
    print(f"    η (from direct fit)  = {eta_from_direct:.2f}")
    print(f"    η target zone: [{eta_from_direct:.2f}, {eta_from_compactness:.2f}]")
    
    # ----------------------------------------------------------
    # 7. Correlation Tests (Scatter Validation)
    # ----------------------------------------------------------
    r_inc, p_inc = stats.pearsonr(df["residual"], df["i_deg"])
    
    df["f_gas"] = HI_CORRECTION * df["M_HI"] / df["M_bar"]
    r_gas, p_gas = stats.pearsonr(df["residual"], df["f_gas"])
    
    print(f"\n[7] Scatter validation:")
    print(f"    Inclination:  r = {r_inc:.3f}, p = {p_inc:.2f}")
    print(f"    Gas fraction: r = {r_gas:.3f}, p = {p_gas:.2f}")
    
    # ----------------------------------------------------------
    # 8. BIC Summary
    # ----------------------------------------------------------
    delta_BIC = BIC_LAMBDA - BIC_RAR
    
    print(f"\n[8] BIC Model Comparison:")
    print(f"    BIC(RAR) = {BIC_RAR:.1f}")
    print(f"    BIC(λ)   = {BIC_LAMBDA:.1f}")
    print(f"    ΔBIC     = +{delta_BIC:.0f}")
    print(f"    → RAR decisively preferred")
    
    # ----------------------------------------------------------
    # 9. Create Output Archive
    # ----------------------------------------------------------
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Canonical JSON
    canonical = {
        "N": N,
        "median_lambda": float(median_lambda),
        "log10_median_lambda": round(log_median, 2),
        "slope_s": round(s, 3),
        "slope_s_err": round(s_err, 3),
        "alpha_direct": round(alpha_direct, 3),
        "alpha_direct_err": round(alpha_direct_err, 3),
        "alpha_inferred": round(alpha_infer, 3),
        "eta_target_zone": [round(eta_from_direct, 2), round(eta_from_compactness, 2)],
        "eta_from_compactness": round(eta_from_compactness, 2),
        "eta_from_direct": round(eta_from_direct, 2),
        "scatter_dex": round(scatter_dex, 2),
        "r_inclination": round(r_inc, 3),
        "p_inclination": round(p_inc, 2),
        "r_gas_fraction": round(r_gas, 3),
        "p_gas_fraction": round(p_gas, 2),
        "ΔBIC": int(delta_BIC),
        "BIC_inputs": {
            "BIC_RAR": BIC_RAR,
            "BIC_lambda": BIC_LAMBDA,
            "n": N_RC_POINTS,
            "k_RAR": K_RAR,
            "k_lambda": K_LAMBDA
        },
        "mass_range_Msun": [float(df["M_bar"].min()), float(df["M_bar"].max())],
        "lambda_range": [float(df["lambda"].min()), float(df["lambda"].max())],
        "code_version": "SPARC_Compactness_v3.1"
    }
    
    canonical_path = os.path.join(OUTPUT_DIR, "canonical_FINAL_v3.1.json")
    with open(canonical_path, "w") as f:
        json.dump(canonical, f, indent=2)
    print(f"\n[9] Saved: {canonical_path}")
    
    # BIC Verification JSON
    bic_summary = {
        "metadata": {
            "description": "Bayesian Model Comparison: RAR vs λ-scaling",
            "date": "2026-01-05",
            "methodology": "Maximum Likelihood Estimation"
        },
        "models": {
            "M0_RAR": {"BIC": BIC_RAR, "k": K_RAR},
            "M1_Lambda": {"BIC": BIC_LAMBDA, "k": K_LAMBDA}
        },
        "n_data_points": N_RC_POINTS,
        "delta_BIC": int(delta_BIC),
        "verdict": "RAR decisively preferred (ΔBIC >> 10)",
        "interpretation": "Global compactness carries no predictive dynamical power"
    }
    
    bic_path = os.path.join(OUTPUT_DIR, "BIC_Verification_summary.json")
    with open(bic_path, "w") as f:
        json.dump(bic_summary, f, indent=2)
    print(f"    Saved: {bic_path}")
    
    # ----------------------------------------------------------
    # 10. Generate Checksums
    # ----------------------------------------------------------
    checksums = []
    for fname in os.listdir(OUTPUT_DIR):
        if fname != "CHECKSUMS.txt":
            fpath = os.path.join(OUTPUT_DIR, fname)
            if os.path.isfile(fpath):
                checksum = sha256_file(fpath)
                checksums.append(f"{checksum}  {fname}")
    
    checksum_path = os.path.join(OUTPUT_DIR, "CHECKSUMS.txt")
    with open(checksum_path, "w") as f:
        f.write("\n".join(checksums))
    print(f"    Saved: {checksum_path}")
    
    # ----------------------------------------------------------
    # Summary
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("CANONICAL VALUES SUMMARY")
    print("=" * 60)
    print(f"  N                  = {N}")
    print(f"  Median λ           = {median_lambda:.2e}")
    print(f"  log₁₀(median λ)    = {log_median:.2f}")
    print(f"  Slope s            = {s:.3f} ± {s_err:.3f}")
    print(f"  α_direct           = {alpha_direct:.3f} ± {alpha_direct_err:.3f}")
    print(f"  α_inferred         = {alpha_infer:.3f}")
    print(f"  η target zone      = [{eta_from_direct:.2f}, {eta_from_compactness:.2f}]")
    print(f"  Scatter σ          = {scatter_dex:.2f} dex")
    print(f"  ΔBIC               = +{delta_BIC:.0f}")
    print("=" * 60)
    print("✅ Analysis complete. Archive ready for publication.")
    
    return canonical

if __name__ == "__main__":
    main()
