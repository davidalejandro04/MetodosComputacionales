"""
Statistical Distributions and the Central Limit Theorem
=========================================================
Part 1 — Exponential Distribution:
  Generates 100 samples from Exp(λ=1), fits the distribution
  using scipy.stats, and overlays the fitted PDF on a histogram.

Part 2 — Central Limit Theorem (CLT):
  For each of 1 000 trials, draws 1 000 samples from Exp(1) and
  computes their sum. By the CLT, this sum should be approximately
  Normal(μ=1000, σ²=1000). The normal fit is overlaid on the
  histogram of sums.

Outputs saved to outputs/:
  - exponential_distribution.png
  - central_limit_theorem.png
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import expon, norm
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

rng = np.random.default_rng(seed=42)  # reproducible results

# ── Part 1: Exponential Distribution ─────────────────────────────────────────
samples_exp = rng.exponential(scale=1.0, size=100)
loc_fit, scale_fit = expon.fit(samples_exp)

x_exp = np.linspace(0, 15, 1000)
pdf_exp = expon.pdf(x_exp, loc_fit, scale_fit)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(samples_exp, bins=20, density=True, color='tomato', alpha=0.6,
        edgecolor='white', label="Samples (n=100)")
ax.plot(x_exp, pdf_exp, 'k-', lw=2,
        label=r"Fitted Exp($\lambda$=%.2f)" % (1.0 / scale_fit))
ax.set_xlabel("x"); ax.set_ylabel("Density")
ax.set_title("Exponential Distribution — Histogram & Fitted PDF")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "exponential_distribution.png"), dpi=150)
print("Saved outputs/exponential_distribution.png")
plt.close()

# ── Part 2: Central Limit Theorem ────────────────────────────────────────────
N_TRIALS  = 1_000
N_SAMPLES = 1_000

sums = np.array([
    rng.exponential(scale=1.0, size=N_SAMPLES).sum()
    for _ in range(N_TRIALS)
])

mu_fit, sigma_fit = norm.fit(sums)
print(f"\nCLT: sum of {N_SAMPLES} Exp(1) variables")
print(f"  Empirical mean  = {sums.mean():.2f}   (expected {N_SAMPLES:.0f})")
print(f"  Empirical std   = {sums.std():.2f}    (expected {N_SAMPLES**0.5:.2f})")
print(f"  Fitted Normal   = N({mu_fit:.2f}, {sigma_fit:.2f})")

x_clt = np.linspace(sums.min(), sums.max(), 1000)
pdf_clt = norm.pdf(x_clt, mu_fit, sigma_fit)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(sums, bins=50, density=True, color='royalblue', alpha=0.6,
        edgecolor='white', label=f"Sum of {N_SAMPLES} Exp(1)  (n={N_TRIALS} trials)")
ax.plot(x_clt, pdf_clt, 'k-', lw=2,
        label=r"Fitted Normal $\mathcal{N}$(%.1f, %.1f)" % (mu_fit, sigma_fit))
ax.set_xlabel("Sum"); ax.set_ylabel("Density")
ax.set_title("Central Limit Theorem — Sum of Exponential Variables")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "central_limit_theorem.png"), dpi=150)
print("Saved outputs/central_limit_theorem.png")
plt.close()
