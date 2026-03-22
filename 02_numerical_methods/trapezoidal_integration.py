"""
Trapezoidal Rule Integration — cos(x)
=======================================
Numerically integrates f(x) = cos(x) over a user-defined interval
[a, b] using the composite trapezoidal rule with N sample points.

The filled area between the curve and the x-axis is visualised and
saved to outputs/trapezoidal_integration.png.

Usage:
    python trapezoidal_integration.py
    # → prompts for a, b, N
    # Or run non-interactively with defaults (0, π/2, 500)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fx(x: np.ndarray) -> np.ndarray:
    """Function to integrate."""
    return np.cos(x)


def trapezoidal(a: float, b: float, N: int) -> float:
    """Composite trapezoidal rule for fx over [a, b] with N points.

    Args:
        a: Left endpoint.
        b: Right endpoint.
        N: Number of sample points (N-1 sub-intervals).

    Returns:
        Numerical approximation of the integral.
    """
    h = (b - a) / (N - 1)
    x = np.linspace(a, b, N)
    y = fx(x)
    return float(np.sum(h * y) - (h / 2) * y[0] - (h / 2) * y[-1])


# ── Get integration bounds ───────────────────────────────────────────────────
try:
    a = float(input("Enter lower bound a (default 0): ") or 0)
    b = float(input("Enter upper bound b (default π/2 ≈ 1.5708): ") or np.pi / 2)
    N = int(input("Enter number of points N (default 500): ") or 500)
except (ValueError, EOFError):
    a, b, N = 0.0, np.pi / 2, 500

integral = trapezoidal(a, b, N)
analytical = np.sin(b) - np.sin(a)   # exact value

print("\nIntegral of cos(x) from %.4f to %.4f" % (a, b))
print("  Numerical  : %.10f  (N = %d)" % (integral, N))
print("  Analytical : %.10f" % analytical)
print("  Error      : %.2e" % abs(integral - analytical))

# ── Plot ─────────────────────────────────────────────────────────────────────
x_plot = np.linspace(a, b, N)
y_plot = fx(x_plot)

fig, ax = plt.subplots(figsize=(7, 5))
ax.fill_between(x_plot, 0, y_plot, alpha=0.35, color="darkorange",
                label="Area ≈ %.6f" % integral)
ax.plot(x_plot, y_plot, color="darkorange", lw=2, label=r"$f(x) = \cos(x)$")
ax.axhline(0, color="black", lw=0.8)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_title(r"Trapezoidal Integration of $\cos(x)$ on [%.3g, %.3g]" % (a, b))
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "trapezoidal_integration.png"), dpi=150)
print("Figure saved to outputs/trapezoidal_integration.png")
plt.close()
