"""
Numerical Differentiation — Error Analysis
============================================
Compares the truncation error of four finite-difference schemes
for f(x) = e^{-x} against the analytical derivative f'(x) = -e^{-x}.

Methods compared:
  1. Forward difference  — O(h)   : [f(x+h) - f(x)] / h
  2. Backward difference — O(h)   : [f(x) - f(x-h)] / h
  3. Central difference  — O(h²)  : [f(x+h/2) - f(x-h/2)] / h
  4. Richardson extrap.  — O(h⁴)  : (4·C(h/2) - C(h)) / 3

A 3-D surface plot (log₁₀ error vs x vs log₁₀ h) is saved to
outputs/differentiation_error.png.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401 (registers 3-D projection)
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ── Target function & analytical derivative ──────────────────────────────────
def fx(x):
    return np.exp(-x)

def fx_prime(x):
    """Analytical first derivative of fx."""
    return -np.exp(-x)


# ── Numerical differentiation schemes ────────────────────────────────────────
def differentiate(method: int, x, h):
    """Return the numerical derivative of fx at x with step h.

    Args:
        method: 1=forward, 2=backward, 3=central, 4=Richardson
    """
    if method == 1:
        return (fx(x + h) - fx(x)) / h
    if method == 2:
        return (fx(x) - fx(x - h)) / h
    if method == 3:
        return (fx(x + h / 2) - fx(x - h / 2)) / h
    if method == 4:
        C_half = (fx(x + h / 4) - fx(x - h / 4)) / (h / 2)
        C_full = (fx(x + h / 2) - fx(x - h / 2)) / h
        return (4 * C_half - C_full) / 3


def absolute_error(analytical, numerical):
    return np.abs(analytical - numerical)


# ── Build 2-D grid of (x, h) values ─────────────────────────────────────────
x_vals = np.linspace(-10, 10, 100)
h_vals = np.logspace(-10, 0, 300)
X, H   = np.meshgrid(x_vals, h_vals)

analytical = fx_prime(X)

# ── Plot — 3-D error surfaces ─────────────────────────────────────────────────
fig = plt.figure(figsize=(12, 7))
ax  = fig.add_subplot(111, projection='3d')

configs = [
    (1, "Forward  O(h)",       "royalblue"),
    (2, "Backward O(h)",       "tomato"),
    (3, "Central  O(h²)",      "gold"),
    (4, "Richardson O(h⁴)",    "mediumpurple"),
]

for method, label, color in configs:
    err = absolute_error(analytical, differentiate(method, X, H))
    # Clip to avoid log(0) issues
    log_err = np.log10(np.clip(err, 1e-16, None))
    ax.plot_surface(X, np.log10(H), log_err,
                    rstride=5, cstride=5,
                    color=color, alpha=0.55, label=label)

ax.set_xlabel("x")
ax.set_ylabel("log₁₀(h)")
ax.set_zlabel("log₁₀(|error|)")
ax.set_title("Differentiation Error vs Step Size  (f(x) = e^{-x})")

# Manual legend proxies (plot_surface doesn't support legend natively)
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=c, label=l) for _, l, c in configs]
ax.legend(handles=legend_elements, loc="upper left")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "differentiation_error.png"), dpi=150)
print("Figure saved to outputs/differentiation_error.png")
plt.close()
