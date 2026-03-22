"""
Covariance Matrix and Principal Component Analysis (PCA)
==========================================================
Loads room temperature readings from four sensors (Front-Left,
Front-Right, Back-Left, Back-Right), computes the covariance matrix
manually, performs eigendecomposition, and projects the data onto
the first two principal components.

Data file: ../data/roomtemperature.csv
Output: outputs/covariance_pca.png
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "roomtemperature.csv")

# ── Load sensor data ─────────────────────────────────────────────────────────
# Columns 1-4: FrontLeft, FrontRight, BackLeft, BackRight  (in Kelvin)
data = np.genfromtxt(DATA_FILE, delimiter=',', skip_header=1, usecols=(1, 2, 3, 4))
n_samples, n_dims = data.shape
sensor_labels = ["Front-Left", "Front-Right", "Back-Left", "Back-Right"]

print("Data shape:", data.shape)
print("Mean temperatures (K):", np.mean(data, axis=0).round(2))

# ── Manual covariance matrix ─────────────────────────────────────────────────
cov = np.zeros((n_dims, n_dims))
for i in range(n_dims):
    for j in range(n_dims):
        ti = data[:, i] - np.mean(data[:, i])
        tj = data[:, j] - np.mean(data[:, j])
        cov[i, j] = np.dot(ti, tj) / (n_samples - 1)

print("\nCovariance matrix:")
print(cov.round(4))

# ── Eigendecomposition ───────────────────────────────────────────────────────
eigenvalues, eigenvectors = np.linalg.eig(cov)

# Sort in descending order of explained variance
order       = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[order]
eigenvectors = eigenvectors[:, order]

explained_var = eigenvalues / eigenvalues.sum() * 100
print("\nEigenvalues (explained variance %):")
for k, (val, pct) in enumerate(zip(eigenvalues, explained_var)):
    print(f"  PC{k+1}: {val:.4f}  ({pct:.1f}%)")

# ── Project data onto first two principal components ─────────────────────────
projected = eigenvectors.T @ data.T   # shape (4, n_samples)

# ── Plot ─────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left panel: scatter in PC space
ax = axes[0]
sc = ax.scatter(projected[0], projected[1], c=np.arange(n_samples),
                cmap='viridis', s=15, alpha=0.7)
plt.colorbar(sc, ax=ax, label="Sample index (time →)")
ax.set_xlabel(f"PC1  ({explained_var[0]:.1f}% variance)")
ax.set_ylabel(f"PC2  ({explained_var[1]:.1f}% variance)")
ax.set_title("PCA — Room Temperature Sensors")
ax.grid(True, alpha=0.3)

# Right panel: covariance matrix heatmap
ax2 = axes[1]
im  = ax2.imshow(cov, cmap='coolwarm', aspect='auto')
plt.colorbar(im, ax=ax2, label="Covariance [K²]")
ax2.set_xticks(range(n_dims)); ax2.set_xticklabels(sensor_labels, rotation=30)
ax2.set_yticks(range(n_dims)); ax2.set_yticklabels(sensor_labels)
ax2.set_title("Covariance Matrix")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "covariance_pca.png"), dpi=150)
print("\nSaved outputs/covariance_pca.png")
plt.close()
