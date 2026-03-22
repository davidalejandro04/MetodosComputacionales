"""
Nonlinear Pendulum Simulation
===============================
Solves the nonlinear pendulum equation of motion:

    d²θ/dt² = −(g/L)·sin(θ)

reformulated as a coupled first-order system:
    dθ/dt  = ω
    dω/dt  = −(g/L)·sin(θ)

using the 4th-order Runge-Kutta (RK4) method.

Outputs (saved to outputs/):
  - pendulum_solution.png   : θ(t) and ω(t) vs time
  - pendulum_trajectory.png : Snapshot of the pendulum position at t_final
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Simulation parameters ────────────────────────────────────────────────────
H   = 0.05          # time step [s]
T0  = 0.0           # start time [s]
TF  = 20.0          # end time [s]
N   = int((TF - T0) / H)

THETA0 = 1.0        # initial angle [rad]
OMEGA0 = 0.0        # initial angular velocity [rad/s]

G = 9.8             # gravitational acceleration [m/s²]
L = 1.0             # pendulum length [m]

# ── ODE right-hand sides ─────────────────────────────────────────────────────
def dtheta_dt(t, theta, omega):
    """dθ/dt = ω"""
    return omega

def domega_dt(t, theta, omega):
    """dω/dt = −(g/L)·sin(θ)"""
    return -(G / L) * np.sin(theta)


# ── RK4 solver for coupled system ─────────────────────────────────────────────
def solve_rk4():
    """Integrate the pendulum ODE and return time, angle, and angular velocity."""
    t     = np.zeros(N)
    theta = np.zeros(N)
    omega = np.zeros(N)

    t[0], theta[0], omega[0] = T0, THETA0, OMEGA0

    for i in range(1, N):
        ti, th, om = t[i-1], theta[i-1], omega[i-1]

        k1 = H * dtheta_dt(ti,         th,           om          )
        l1 = H * domega_dt(ti,         th,           om          )
        k2 = H * dtheta_dt(ti+H*0.5,   th+k1*0.5,   om+l1*0.5   )
        l2 = H * domega_dt(ti+H*0.5,   th+k1*0.5,   om+l1*0.5   )
        k3 = H * dtheta_dt(ti+H*0.5,   th+k2*0.5,   om+l2*0.5   )
        l3 = H * domega_dt(ti+H*0.5,   th+k2*0.5,   om+l2*0.5   )
        k4 = H * dtheta_dt(ti+H,       th+k3,        om+l3       )
        l4 = H * domega_dt(ti+H,       th+k3,        om+l3       )

        theta[i] = th + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        omega[i] = om + (l1 + 2*l2 + 2*l3 + l4) / 6.0
        t[i]     = ti + H

    return t, theta, omega


# ── Solve ────────────────────────────────────────────────────────────────────
t, theta, omega = solve_rk4()

# Cartesian position of the pendulum bob
bob_x = -L * np.sin(theta)
bob_y =  THETA0 - L * np.cos(theta)   # measured from pivot at y=THETA0

# ── Plot 1: θ(t) and ω(t) vs time ────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, theta, color='royalblue', lw=1.5)
ax1.set_ylabel(r"$\theta$ [rad]")
ax1.set_title(r"Nonlinear Pendulum  ($\theta_0 = %.1f$ rad,  $L = %.1f$ m)" % (THETA0, L))
ax1.axhline(0, color='k', lw=0.5, ls='--')
ax1.grid(True, alpha=0.3)

ax2.plot(t, omega, color='tomato', lw=1.5)
ax2.set_xlabel("Time [s]")
ax2.set_ylabel(r"$\omega$ [rad/s]")
ax2.axhline(0, color='k', lw=0.5, ls='--')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "pendulum_solution.png"), dpi=150)
print("Saved outputs/pendulum_solution.png")
plt.close()

# ── Plot 2: pendulum bob trajectory (x-y path) ───────────────────────────────
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(bob_x, bob_y, color='royalblue', lw=0.8, alpha=0.6, label="Trajectory")
ax.plot(0, THETA0, 'ks', ms=8, label="Pivot")                 # pivot point
ax.plot(bob_x[-1], bob_y[-1], 'ro', ms=10, label="Final pos") # final position

ax.set_xlabel("x [m]"); ax.set_ylabel("y [m]")
ax.set_title("Pendulum Bob Trajectory")
ax.set_aspect('equal')
ax.legend(); ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "pendulum_trajectory.png"), dpi=150)
print("Saved outputs/pendulum_trajectory.png")
plt.close()
