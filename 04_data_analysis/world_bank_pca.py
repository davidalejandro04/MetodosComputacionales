"""
World Bank Data — Exploratory Analysis and PCA
================================================
Reads socioeconomic indicator data from the World Bank dataset
(DatosBancoMundial5.csv) covering five variables per country:

  1. Tax Rate (% of commercial profit)
  2. Cost of Business Start-Up (% GNI per capita)
  3. Female Unemployment Rate (%)
  4. Male Unemployment Rate (%)
  5. Ratio of Female-to-Male Labour Force Participation

Steps:
  1. Z-score normalisation of each indicator
  2. Histogram exploration of normalised distributions
  3. Manual covariance matrix computation
  4. Eigendecomposition and extraction of principal components
  5. Scatter plots of data and variable loadings in PC space

Outputs saved to outputs/:
  - world_bank_data_histograms.png
  - world_bank_pca_data.png
  - world_bank_pca_variables.png

Requires: DatosBancoMundial5.csv (place in the same directory).
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

DATA_FILE = os.path.join(os.path.dirname(__file__), "DatosBancoMundial5.csv")

# ── Load data ────────────────────────────────────────────────────────────────
if not os.path.exists(DATA_FILE):
    print("ERROR: DatosBancoMundial5.csv not found in 04_data_analysis/")
    print("Place the file there and re-run this script.")
    sys.exit(1)

raw = np.array(pd.read_csv(DATA_FILE, skiprows=1, header=None))
a   = raw[:, 4:].astype(float)   # columns 4+ are numeric indicators

VARIABLE_LABELS = [
    "Tax Rate",
    "Cost of Business Start-Up",
    "Unemployment (female)",
    "Unemployment (male)",
    "Female/Male Labour Ratio",
]
COLORS = ["crimson", "royalblue", "goldenrod", "seagreen", "mediumpurple"]

# ── Z-score normalisation (row-wise: each country's indicators) ──────────────
Z = np.zeros_like(a)
for i in range(Z.shape[0]):
    Z[i] = (a[i] - np.mean(a[i])) / np.std(a[i])

# ── 1. Histogram of normalised indicators ────────────────────────────────────
fig, axes = plt.subplots(5, 1, figsize=(9, 12), sharex=False)
fig.suptitle("Normalised World Bank Indicators", fontsize=13, y=1.01)

for idx, (ax, label, color) in enumerate(zip(axes, VARIABLE_LABELS, COLORS)):
    ax.hist(Z[idx], bins=25, color=color, alpha=0.75, edgecolor='white')
    ax.set_title(label, fontsize=10)
    ax.set_ylabel("Count")
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "world_bank_data_histograms.png"), dpi=150)
print("Saved outputs/world_bank_data_histograms.png")
plt.close()

# ── 2. Covariance matrix ────────────────────────────────────────────────────
n_vars = Z.shape[0]
cov    = np.zeros((n_vars, n_vars))
for i in range(n_vars):
    for j in range(n_vars):
        ti, tj = Z[i] - Z[i].mean(), Z[j] - Z[j].mean()
        cov[i, j] = np.dot(ti, tj) / (Z.shape[1] - 1)
print("\nCovariance matrix:\n", cov.round(3))

# ── 3. Eigendecomposition ────────────────────────────────────────────────────
eigenvalues, eigenvectors = np.linalg.eig(cov)
order        = eigenvalues.argsort()[::-1]
eigenvalues  = eigenvalues[order]
eigenvectors = eigenvectors[:, order]

explained = eigenvalues / eigenvalues.sum() * 100
print("\nExplained variance per component:")
for k, (val, pct) in enumerate(zip(eigenvalues, explained)):
    print(f"  PC{k+1}: eigenvalue={val:.3f}, explained={pct:.1f}%")

# ── 4. Project data onto PC1 and PC2 ────────────────────────────────────────
projected = eigenvectors.T @ Z          # shape (n_vars, n_countries)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(projected[0], projected[1], s=15, alpha=0.6, color='royalblue', label="Countries")
ax.set_xlabel(f"PC1  ({explained[0]:.1f}% variance)")
ax.set_ylabel(f"PC2  ({explained[1]:.1f}% variance)")
ax.set_title("World Bank Data — Countries in Principal Component Space")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "world_bank_pca_data.png"), dpi=150)
print("Saved outputs/world_bank_pca_data.png")
plt.close()

# ── 5. Variable loadings in PC space ─────────────────────────────────────────
# Project the original variables (rows of Z) through the PCA transformation
var_projected = projected @ Z.T         # shape (n_vars, n_vars)

fig, ax = plt.subplots(figsize=(8, 6))
for idx, (label, color) in enumerate(zip(VARIABLE_LABELS, COLORS)):
    ax.scatter(var_projected[0, idx], var_projected[1, idx],
               s=120, color=color, label=label, zorder=3)

ax.set_xlabel(f"PC1  ({explained[0]:.1f}% variance)")
ax.set_ylabel(f"PC2  ({explained[1]:.1f}% variance)")
ax.set_title("World Bank Variables — Loadings in PC Space")
ax.legend(loc="best", fontsize=8)
ax.axhline(0, color='k', lw=0.6, ls='--')
ax.axvline(0, color='k', lw=0.6, ls='--')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "world_bank_pca_variables.png"), dpi=150)
print("Saved outputs/world_bank_pca_variables.png")
plt.close()
