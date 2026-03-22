"""
Approximation of π via Trapezoidal Integration
================================================
Integrates f(x) = 4√(1 − x²) over [0, 1], which equals the area of
a quarter circle of radius 1, giving π.

    π ≈ ∫₀¹ 4√(1 − x²) dx

The trapezoidal rule is applied with N = 10 000 sub-intervals.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fx(x: np.ndarray) -> np.ndarray:
    """Quarter-circle function whose integral over [0,1] equals π."""
    return 4 * np.sqrt(1 - x ** 2)


def trapezoidal(a: float, b: float, N: int) -> float:
    """Approximate ∫ₐᵇ f(x) dx using the composite trapezoidal rule.

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
    # Trapezoidal sum: h*Σy  −  h/2·y[0]  −  h/2·y[-1]
    return float(np.sum(h * y) - (h / 2) * y[0] - (h / 2) * y[-1])


# ── Compute π ────────────────────────────────────────────────────────────────
a, b, N = 0.0, 1.0, 10_000
pi_approx = trapezoidal(a, b, N)
print("pi ~= %.10f  (N = %d)" % (pi_approx, N))
print("pi  = %.10f  (numpy)" % np.pi)
print("Error = %.2e" % abs(pi_approx - np.pi))

# ── Plot ─────────────────────────────────────────────────────────────────────
x_plot = np.linspace(a, b, N)
y_plot = fx(x_plot)

fig, ax = plt.subplots(figsize=(7, 5))
ax.fill_between(x_plot, 0, y_plot, alpha=0.35, color="steelblue", label="Area ≈ π")
ax.plot(x_plot, y_plot, color="steelblue", lw=2)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x) = 4\sqrt{1-x^2}$")
ax.set_title(r"Approximating $\pi$ via the Trapezoidal Rule   ($\pi \approx %.6f$)" % pi_approx)
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "pi_approximation.png"), dpi=150)
print("Figure saved to outputs/pi_approximation.png")
plt.close()
