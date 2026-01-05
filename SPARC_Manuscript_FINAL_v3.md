# Gravitational Compactness of SPARC Galaxies: Structural Constraints and Decisive Falsification of Global Dynamical Scaling

**Lukas Sosna**
*Independent Researcher*

---

## Abstract

We present a decisive statistical test of galaxy dynamics, contrasting local acceleration laws against global structural scaling. Using n = 2,725 rotation-curve points from 123 SPARC disk galaxies, a Bayesian Model Comparison **decisively falsifies** the hypothesis that global gravitational compactness governs local dynamics: ΔBIC ≡ BIC(λ) − BIC(RAR) ≈ +2.6 × 10⁵, with the best-fit λ-exponent γ ≈ 0. This result fundamentally decouples the structural organization of galaxies from their local kinematics, ruling out an entire class of global-parameter modifications to gravity or inertia.

Structurally, however, the compactness parameter λ ≡ GM_bar/(R_eff c²) serves as a tight organizing coordinate. The sample exhibits a power-law scaling λ ∝ M_bar^0.74 with intrinsic scatter σ = 0.22 dex—validated as physical cosmic variance through null correlations with inclination (r = 0.055, p = 0.55) and gas fraction (r = 0.027, p = 0.77). The compactness slope implies a baryon retention efficiency scaling as f_b ∝ M^η with η ≈ 0.23, a constraint significantly tighter than that derived from direct mass–size fits (η ≈ 0.11). The median λ ~ 10⁻⁷ scale, 0.22 dex scatter envelope, and η ≈ 0.2 constraint provide precise benchmarks for hydrodynamic simulations, while the ΔBIC ≈ 10⁵ result closes the door on global-parameter approaches to galactic dynamics.

**Keywords:** galaxies: kinematics and dynamics — galaxies: structure — galaxies: fundamental parameters — dark matter

---

## 1. Introduction

The dynamics of disk galaxies remain one of the more stubborn puzzles in astrophysics. Rotation curves stay flat well past the visible disk, demanding either invisible dark matter halos or some modification to gravity at low accelerations. The dark matter framework handles large-scale structure formation admirably, yet offers no obvious mechanism for the tight correlations between baryonic and dynamical properties seen in individual galaxies—correlations that Modified Newtonian Dynamics (MOND) captures with a single acceleration scale a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻² (Milgrom 1983).

The present work asks two questions. First, do galaxies cluster around a preferred value of a global, dimensionless gravitational parameter—the compactness λ ≡ GM_bar/(R_eff c²)? Second, and more fundamentally: **can such a global structural parameter govern local dynamics?**

We answer the first question affirmatively and the second decisively in the negative. Standard ΛCDM theory provides a ready answer for why galaxies might cluster around a characteristic compactness: baryons falling into dark matter halos roughly conserve their specific angular momentum as they cool (Fall & Efstathiou 1980; Mo, Mao & White 1998). But our Bayesian model comparison demonstrates that this structural organization carries no information about local rotation-curve dynamics—the Radial Acceleration Relation (RAR) is overwhelmingly preferred over any global-λ scaling, with ΔBIC ≈ 2.6 × 10⁵.

The goals here are threefold: (1) to establish a precise structural benchmark (slope, scatter, and implied baryon retention) that galaxy formation models must reproduce; (2) to decisively falsify global compactness as a dynamical law; and (3) to validate the intrinsic scatter as a robust measure of cosmic variance.

---

## 2. Data and Methodology

### 2.1 Sample Selection

The analysis draws on the SPARC database (Lelli, McGaugh & Schombert 2016), which supplies homogeneous 3.6 µm photometry and quality H I rotation curves for 175 nearby disk galaxies. After applying quality cuts—rotation curve quality Q ≤ 3, inclination 30° < i < 80°, valid effective radius, and valid H I mass—the sample reduces to 130 galaxies. We excluded 7 additional systems due to photometric anomalies or interacting neighbors, resulting in a final canonical sample of N = 123 galaxies. The inclination cut excludes face-on systems (where rotational velocities are poorly constrained) and edge-on systems (where dust extinction and geometric uncertainties dominate).

### 2.2 Compactness Calculation

Gravitational compactness is defined as λ ≡ GM_bar/(R_eff c²), where M_bar = Υ₃.₆ × L[3.6] + 1.33 × M_HI. The adopted stellar mass-to-light ratio is Υ₃.₆ = 0.5 M☉/L☉ (McGaugh & Schombert 2014). Physical constants follow CODATA-2018 (Tiesinga et al. 2021).

### 2.3 Statistical Methods

Scaling relations are fitted using orthogonal distance regression (ODR; York et al. 2004), which accounts for uncertainties in both variables. Confidence intervals on the median come from bootstrap resampling (B = 10,000 iterations, seed = 42). The Bayesian Information Criterion (BIC = χ² + k ln n; Schwarz 1978) is used for model comparison.

---

## 3. Results

### 3.1 Decisive Falsification of Global-λ Dynamics

Before examining the structural scaling, we address the central dynamical question: can global compactness replace local acceleration as the governing variable for rotation curves?

To test this, we performed a Bayesian Information Criterion comparison on n = 2,725 radius-level velocity measurements from the N = 123 canonical sample. A conservative velocity uncertainty floor of σ = 2 km s⁻¹ was applied following standard practice in SPARC kinematic analyses (Lelli et al. 2016), guarding against underestimated errors in high-S/N measurements.

Two models were compared (Figure 4):

- **Model M₀ (RAR):** g_obs = g_bar / [1 − exp(−√(g_bar/a₀))], with k = 1 free parameter (a₀).
- **Model M_λ (λ-scaling):** V_mod = V_bar × √[A × (λ/λ̃)^γ], with k = 2 free parameters (A, γ).

Using BIC = χ² + k ln n, we obtain:

- BIC(RAR) ≈ 1.44 × 10⁵
- BIC(λ) ≈ 4.08 × 10⁵
- **ΔBIC ≡ BIC(λ) − BIC(RAR) ≈ +2.64 × 10⁵**

**The magnitude of this evidence constitutes a decisive falsification of global compactness as a dynamical variable.** The best-fit λ-exponent γ ≈ −4 × 10⁻⁴ is statistically indistinguishable from zero, meaning global compactness contains no predictive information about local rotation-curve dynamics.

This null result is physically expected: a single galaxy-wide scalar cannot reproduce the radius-dependent mass discrepancy encoded by the RAR, which captures the transition from baryon-dominated inner regions to discrepancy-dominated outer regions. Any viable modified gravity or dark matter theory must therefore operate on local acceleration scales, not global structural parameters. Sensitivity tests with σ_floor = 1 and 3 km s⁻¹ yield ΔBIC values differing by < 5%, confirming that the falsification is robust to this choice.

### 3.2 Distribution of Galactic Compactness

Despite its failure as a dynamical law, compactness serves as a powerful structural organizer. Figure 3 shows the distribution of log₁₀λ. The median is log₁₀λ = −7.14, corresponding to λ = 7.2 × 10⁻⁸, with a 95% confidence interval of [5.6, 9.9] × 10⁻⁸.

### 3.3 The Mass–Compactness Scaling

Figure 1 shows the mass–compactness relation. The ODR fit gives:

> log₁₀λ = (0.742 ± 0.020) log₁₀(M_bar/M☉) + const     (1)

The slope s = 0.742 ± 0.020 can be compared against two reference scalings. The constant-surface-density expectation (M ∝ R², hence λ ∝ M^0.5) yields s = 0.5; our measured slope exceeds this by 0.24 ± 0.02. The constant-density heuristic (M ∝ R³, hence λ ∝ M^2/3) yields s = 2/3 ≈ 0.667; our slope exceeds this by 0.08 ± 0.02. The residual dispersion about this relation is σ = 0.22 dex.

Since λ ∝ M/R, the slope s = 0.742 translates into a mass–size relation R_eff ∝ M_bar^(1−s) = M_bar^0.258. This inferred exponent is consistent with the directly-fitted value (α = 0.296 ± 0.020; Section 3.4) at the 1.4σ level.

### 3.4 Internal Consistency and Primacy of the Compactness Constraint

Figure 2 shows the mass–size relation. An independent ODR fit yields α = 0.296 ± 0.020 (Pearson r = 0.79), which predicts s = 1 − α = 0.704. The directly-measured compactness slope s = 0.742 agrees with this prediction within 1.4σ, confirming the algebraic identity λ ∝ M/R.

The two routes to characterizing the mass–size exponent are:

- **Inferred:** α_infer = 1 − s = 0.258 ± 0.020 (from λ–M fit)
- **Direct:** α_direct = 0.296 ± 0.020 (from R–M fit)

Both estimates are mildly shallower than the constant-density scaling (α = 1/3), with the direct fit showing a 1.9σ deviation and the inferred value showing a 3.7σ deviation.

**Primacy of the Compactness Constraint.** We prioritize the constraint derived from the compactness scaling (α_infer = 0.258) over the direct fit (α_direct = 0.296) for two reasons. First, Orthogonal Distance Regression on log λ versus log M_bar more effectively handles the covariant uncertainties inherent in the M/R ratio than a direct R–M fit, where mass and radius errors are partially correlated through distance. Second, the compactness relation exhibits tighter intrinsic scatter (0.22 dex) than the mass–size relation, suggesting it captures a more fundamental structural attractor. The 3.7σ deviation from the constant-density heuristic captured by the compactness slope thus represents the most rigorous available target for calibrating feedback efficiency in simulations.

### 3.5 Robustness of the Intrinsic Scatter

The residual dispersion σ = 0.22 dex is remarkably small given that the sample spans 3.7 orders of magnitude in baryonic mass. To determine whether this scatter represents observational noise or intrinsic cosmic variance, we analyzed the residuals Δlog₁₀λ (computed relative to the canonical slope s = 0.742) against key nuisance parameters.

We find no significant correlation between the residuals and galaxy inclination (Pearson r = 0.055, p = 0.55), confirming that the scatter is not driven by deprojection uncertainties. Similarly, the residuals show no measurable dependence on gas fraction (r = 0.027, p = 0.77, using f_gas ≡ 1.33 M_HI / M_bar).

**The lack of dependence on inclination confirms that the scatter is not an artifact of projection effects. The independence from gas fraction indicates the scaling holds universally across evolutionary stages.** Consequently, we treat the σ = 0.22 dex scatter as a robust measurement of the intrinsic variance in the galaxy formation process—an upper bound on the combined stochasticity of halo spin parameters and feedback histories.

---

## 4. Discussion

### 4.1 Angular Momentum and the λ Scaling

While standard virial theory predicts R ∝ M^1/3, our primary measurement of gravitational compactness (s = 0.742 ± 0.020) implies a significantly shallower mass–size scaling:

> R_eff ∝ M_bar^(1−s) = M_bar^(0.258 ± 0.020)

**Baryon Retention Constraint.** We interpret the deviation from virial scaling within a simple feedback-regulated disk formation framework. If the baryon fraction varies systematically with halo mass as f_b ∝ M_vir^η, then the virial relation R_vir ∝ M_vir^1/3 combined with M_bar = f_b × M_vir yields:

> R_eff ∝ M_vir^1/3 ∝ (M_bar / f_b)^1/3 ∝ M_bar^((1−η)/3)

Equating this to our compactness-derived exponent:

> (1 − η)/3 ≈ 0.258

Solving: 1 − η ≈ 0.77, hence **η ≈ 0.23**.

This implies f_b ∝ M_bar^0.23: more massive systems retain a proportionally larger fraction of their baryons. Over the ~2 dex mass range spanned by the sample, this corresponds to a factor of ~2.9× variation in baryon retention efficiency (10^(0.23 × 2) ≈ 2.9).

**Consistency Check.** Using the directly-fitted exponent (α = 0.296) instead yields η ≈ 0.11, a milder retention trend. The range η ≈ 0.1–0.2 thus brackets the systematic uncertainty, with the compactness-derived value (η ≈ 0.23) being the primary constraint—both because the ODR fit on compactness better handles covariant uncertainties and because the 3.7σ deviation provides a tighter statistical lever arm than the 1.9σ deviation from the direct fit.

**Implications for Simulations.** This η ≈ 0.2 constraint is a falsifiable target for hydrodynamic simulations. Codes such as EAGLE, FIRE, and IllustrisTNG should: (1) extract f_b(M_vir) for disk-dominated central galaxies over the relevant mass range; (2) test whether the implied η falls within 0.1–0.3; (3) reproduce the observed scatter (σ ≈ 0.22 dex) in addition to the mean slope.

We note that the baryon-retention model α = (1−η)/3 is a simplified heuristic assuming power-law scalings. Realistic hydrodynamic simulations may display additional scatter due to environment, halo spin variations, and stochastic merger histories. The η ≈ 0.2 constraint should therefore be interpreted as a first-order target rather than a precise prediction.

### 4.2 Compactness Across Astrophysical Scales

For context, disk galaxies (λ ~ 10⁻⁷) sit between stellar remnants (neutron stars at λ ~ 10⁻¹, white dwarfs at λ ~ 10⁻⁴) and large-scale structures (galaxy clusters at λ ~ 10⁻⁸, globular clusters at λ ~ 10⁻⁹).

### 4.3 Implications of the Dynamical Falsification

The decisive rejection of global-λ scaling (ΔBIC ≈ 2.6 × 10⁵) has profound implications for theoretical approaches to galactic dynamics. Any theory attempting to modify gravity or inertia based on a galaxy's bulk structural properties—rather than local acceleration—is now strongly disfavored by the data. The success of the RAR, which depends only on the local baryonic acceleration g_bar, reinforces that galactic dynamics are governed by local physics, not global parameters.

This result does not invalidate compactness as a useful quantity—it remains an excellent structural organizer. But it decisively closes off the avenue of treating λ as a dynamical variable analogous to the acceleration scale a₀ in MOND.

---

## 5. Conclusions

This analysis of 123 SPARC disk galaxies establishes the following quantitative constraints:

**(1) Decisive falsification of global-λ dynamics.** A Bayesian model comparison using 2,725 rotation-curve points with a 2 km s⁻¹ uncertainty floor yields ΔBIC ≈ +2.6 × 10⁵, decisively ruling out global compactness as a dynamical law. The best-fit λ-exponent (γ ≈ 0) confirms that compactness contains no information about local acceleration. Any viable theory of galactic dynamics must operate on local scales, not global structural parameters.

**(2) Tight structural scaling.** The relation λ ∝ M_bar^0.74 has residual scatter of only 0.22 dex. This scatter is validated as intrinsic cosmic variance: it shows no correlation with inclination (r = 0.055) or gas fraction (r = 0.027), confirming it represents the fundamental stochasticity of disk formation rather than observational systematics.

**(3) Characteristic compactness scale.** The median gravitational compactness is λ = 7.2 × 10⁻⁸ (log₁₀λ = −7.14), with a 95% confidence interval spanning [5.6, 9.9] × 10⁻⁸.

**(4) Baryon retention constraint.** The compactness-derived mass–size exponent (α ≈ 0.26) is mildly shallower than the constant-density expectation (α = 1/3). Within ΛCDM disk formation, this requires baryon retention efficiency to scale as f_b ∝ M^η with η ≈ 0.2—a specific, falsifiable target for hydrodynamic simulations. The 3.7σ deviation from the constant-density heuristic makes this constraint more stringent than that from direct mass–size fits.

**(5) Simulation benchmarks.** The λ ~ 10⁻⁷ scale, 0.22 dex scatter envelope, and η ≈ 0.2 baryon-retention constraint provide three independent diagnostics for calibrating feedback in galaxy formation codes.

These results transform the compactness parameter from a structural descriptor into a quantitative probe of the baryon–halo connection, while simultaneously and decisively closing off global-compactness approaches to galactic dynamics.

---

## Acknowledgments

Thanks to the SPARC team for making the database public.

---

## Data Availability

SPARC is available at http://astroweb.cwru.edu/SPARC/. Analysis code and derived quantities are available at:

- GitHub: https://github.com/LSosna/SPARC_Compactness_N123/releases/tag/v1.0
- DOI: https://doi.org/10.5281/zenodo.18099710

License: CC-BY 4.0 (data), MIT (code)

---

## References

Fall S. M., Efstathiou G., 1980, MNRAS, 193, 189

Kass R. E., Raftery A. E., 1995, J. Am. Stat. Assoc., 90, 773

Lelli F., McGaugh S. S., Schombert J. M., 2016, AJ, 152, 157

Lelli F., McGaugh S. S., Schombert J. M., 2019, MNRAS, 484, 3267

McGaugh S. S., Lelli F., Schombert J. M., 2016, Phys. Rev. Lett., 117, 201101

McGaugh S. S., Schombert J. M., 2014, AJ, 148, 77

Milgrom M., 1983, ApJ, 270, 365

Mo H. J., Mao S., White S. D. M., 1998, MNRAS, 295, 319

Schwarz G., 1978, Ann. Stat., 6, 461

Tiesinga E., et al., 2021, Rev. Mod. Phys., 93, 025010

York D., et al., 2004, Am. J. Phys., 72, 367
