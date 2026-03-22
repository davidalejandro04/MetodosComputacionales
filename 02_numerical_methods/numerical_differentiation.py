"""
Numerical Differentiation
===========================
Computes successive derivatives of a Gaussian function
    f(x) = exp(-x²) / √(2π)
using finite-difference stencils (forward and central differences)
and plots the function together with its 1st–4th order derivatives.

Methods implemented:
  - 1st order: forward difference  (O(h))
  - 1st order: central difference  (O(h²))
  - 2nd order: central difference  (O(h²))
  - Higher orders: recursive application of 1st/2nd order stencils
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')           # non-interactive backend for saving figures
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ── Function definition ──────────────────────────────────────────────────────
def fx(x: np.ndarray) -> np.ndarray:
    """Gaussian bell curve normalised to unit area."""
    return np.exp(-np.array(x) ** 2) / np.sqrt(2 * np.pi)


# ── Differentiation engine ───────────────────────────────────────────────────
def differentiate(y: np.ndarray, x: np.ndarray, order: int, method: int = 0):
    """Numerically differentiate y(x).

    Args:
        y      : Function values at sample points.
        x      : Sample points (uniformly spaced).
        order  : Derivative order (1–4).
        method : 0 = central difference (default), 1 = forward difference.

    Returns:
        (dy, dx): Derivative values and corresponding x coordinates.
    """
    h = x[1] - x[0]

    # Pre-compute both 1st-order stencils
    d_central = (y[2:] - y[:-2]) / (2 * h)
    x_central = x[1:-1]
    d_forward = (y[1:] - y[:-1]) / h
    x_forward = x[:-1]

    # Second-order central difference
    d_second  = (y[2:] + y[:-2] - 2 * y[1:-1]) / h ** 2

    if order > 2:
        # Recursively apply 1st-order differentiation until desired order
        for _ in range(order):
            y, x = differentiate(y, x, 1, method)
        return y, x

    if order == 1:
        if method == 1:
            return d_forward, x_forward
        return d_central, x_central

    # order == 2
    return d_second, x_central


# ── Compute function and its derivatives ─────────────────────────────────────
x = np.linspace(-4, 4, 1000)
y = fx(x)

dy,    dx    = differentiate(fx(x), x, 1, method=1)   # 1st — forward
dyy,   dxx   = differentiate(fx(x), x, 2)              # 2nd — central
dyyy,  dxxx  = differentiate(fx(x), x, 3)              # 3rd — recursive
dyyyy, dxxxx = differentiate(fx(x), x, 4, method=1)   # 4th — recursive

# ── Plot ─────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(x,     y,     label=r"$f(x)$",                      lw=2)
ax.plot(dx,    dy,    label=r"$\frac{df}{dx}$",             lw=1.5)
ax.plot(dxx,   dyy,   label=r"$\frac{d^2 f}{dx^2}$",       lw=1.5)
ax.plot(dxxx,  dyyy,  label=r"$\frac{d^3 f}{dx^3}$",       lw=1.5)
ax.plot(dxxxx, dyyyy, label=r"$\frac{d^4 f}{dx^4}$",       lw=1.5)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"Amplitude")
ax.set_title("Gaussian Function and Its Derivatives (Finite Differences)")
ax.legend(loc="upper right")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "numerical_differentiation.png"), dpi=150)
print("Figure saved to outputs/numerical_differentiation.png")
plt.close()
