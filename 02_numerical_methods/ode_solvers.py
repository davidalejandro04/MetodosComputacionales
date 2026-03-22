"""
Ordinary Differential Equation (ODE) Solvers
==============================================
Part 1 — Single ODE: dy/dx = -y, y(0) = 1  (exact: y = e^{-x})
  Compares three explicit time-stepping schemes:
    • Leap-Frog (2nd order, explicit, non-self-starting)
    • Runge-Kutta 2nd order (RK2 / midpoint method)
    • Runge-Kutta 4th order (RK4 — standard workhorse)

Part 2 — Coupled ODE system (harmonic oscillator):
    dy₁/dx =  y₂
    dy₂/dx = -a·y₁ − b·y₂ + γ·cos(2πx)
  Solved with RK4 for coupled equations.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ═══════════════════════════════════════════════════════════════════════════════
# Part 1 — Single ODE  dy/dx = -y
# ═══════════════════════════════════════════════════════════════════════════════

h  = 0.01
xi, xf = 0.0, 4.0
n  = int((xf - xi) / h)
x_arr = np.zeros(n)
y_arr = np.zeros(n)


def f_prime(x, y):
    """RHS of dy/dx = -y."""
    return -y


def leap_frog() -> tuple:
    """Leap-Frog (two-step) method.  Not self-starting: uses one Euler step."""
    x = x_arr.copy(); y = y_arr.copy()
    x[0], y[0] = xi, 1.0
    x[1] = x[0] + h
    y[1] = y[0] + h * f_prime(x[0], y[0])          # first step: Euler
    for i in range(2, n):
        x[i] = x[i - 2] + h
        y[i] = y[i - 2] + 2.0 * h * f_prime(x[i - 1], y[i - 1])
    return x, y


def rk2() -> tuple:
    """Runge-Kutta 2nd order (midpoint method)."""
    x = x_arr.copy(); y = y_arr.copy()
    x[0], y[0] = xi, 1.0
    for i in range(1, n):
        k1 = h * f_prime(x[i - 1], y[i - 1])
        k2 = h * f_prime(x[i - 1] + h * 0.5, y[i - 1] + k1 * 0.5)
        x[i] = x[i - 1] + h
        y[i] = y[i - 1] + k2
    return x, y


def rk4() -> tuple:
    """Runge-Kutta 4th order (classic four-stage method)."""
    x = x_arr.copy(); y = y_arr.copy()
    x[0], y[0] = xi, 1.0
    for i in range(1, n):
        k1 = h * f_prime(x[i - 1], y[i - 1])
        k2 = h * f_prime(x[i - 1] + h * 0.5, y[i - 1] + k1 * 0.5)
        k3 = h * f_prime(x[i - 1] + h * 0.5, y[i - 1] + k2 * 0.5)
        k4 = h * f_prime(x[i - 1] + h,        y[i - 1] + k3)
        slope = (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        x[i] = x[i - 1] + h
        y[i] = y[i - 1] + slope
    return x, y


# Exact solution for comparison
x_exact = np.linspace(xi, xf, 500)
y_exact = np.exp(-x_exact)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(x_exact, y_exact, 'k--', lw=1.5, label="Exact $e^{-x}$")
ax.plot(*leap_frog(), color='tomato',     lw=1.5, label="Leap-Frog")
ax.plot(*rk2(),       color='goldenrod',  lw=1.5, label="RK2")
ax.plot(*rk4(),       color='royalblue',  lw=1.5, label="RK4")

ax.set_xlabel(r"$x$"); ax.set_ylabel(r"$y$")
ax.set_title(r"$dy/dx = -y$  —  Numerical vs Exact Solution")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "ode_single.png"), dpi=150)
print("Figure saved to outputs/ode_single.png")
plt.close()


# ═══════════════════════════════════════════════════════════════════════════════
# Part 2 — Coupled system (harmonic oscillator / damped-driven)
# ═══════════════════════════════════════════════════════════════════════════════

h2   = 0.1
xi2, xf2 = 0.0, 20.0
n2   = int((xf2 - xi2) / h2)

# Parameters — modify to explore different regimes
a = 1.0   # spring constant
b = 0.0   # damping coefficient
g = 0.0   # driving amplitude

y1 = np.zeros(n2)
y2 = np.zeros(n2)
x2 = np.zeros(n2)


def f1(xp, yp1, yp2):
    """dy₁/dx = y₂"""
    return yp2


def f2(xp, yp1, yp2):
    """dy₂/dx = -a·y₁ − b·y₂ + γ·cos(2πx)"""
    return -a * yp1 - b * yp2 + g * np.cos(2 * np.pi * xp)


def rk4_coupled():
    """RK4 for the coupled two-equation system."""
    x2[0], y1[0], y2[0] = xi2, 1.0, 0.01
    for i in range(1, n2):
        k1 = h2 * f1(x2[i-1], y1[i-1], y2[i-1])
        l1 = h2 * f2(x2[i-1], y1[i-1], y2[i-1])
        k2 = h2 * f1(x2[i-1]+h2*0.5, y1[i-1]+k1*0.5, y2[i-1]+l1*0.5)
        l2 = h2 * f2(x2[i-1]+h2*0.5, y1[i-1]+k1*0.5, y2[i-1]+l1*0.5)
        k3 = h2 * f1(x2[i-1]+h2*0.5, y1[i-1]+k2*0.5, y2[i-1]+l2*0.5)
        l3 = h2 * f2(x2[i-1]+h2*0.5, y1[i-1]+k2*0.5, y2[i-1]+l2*0.5)
        k4 = h2 * f1(x2[i-1]+h2,     y1[i-1]+k3,     y2[i-1]+l3)
        l4 = h2 * f2(x2[i-1]+h2,     y1[i-1]+k3,     y2[i-1]+l3)

        y1[i] = y1[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        y2[i] = y2[i-1] + (l1 + 2*l2 + 2*l3 + l4) / 6.0
        x2[i] = x2[i-1] + h2


rk4_coupled()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
ax1.plot(x2, y1, color="royalblue", lw=1.5, label=r"$y_1$ (position)")
ax1.set_ylabel(r"$y_1$"); ax1.legend(); ax1.grid(True, alpha=0.3)
ax1.set_title(r"Coupled ODE — Harmonic Oscillator  ($a=%.0f,\ b=%.0f,\ \gamma=%.0f$)" % (a, b, g))

ax2.plot(x2, y2, color="tomato", lw=1.5, label=r"$y_2$ (velocity)")
ax2.set_xlabel(r"$x$"); ax2.set_ylabel(r"$y_2$")
ax2.legend(); ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "ode_coupled.png"), dpi=150)
print("Figure saved to outputs/ode_coupled.png")
plt.close()
