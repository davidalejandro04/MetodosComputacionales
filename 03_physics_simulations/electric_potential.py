"""
Electric Potential and Field Visualisation
============================================
Models four equal point charges placed at the corners of a square
domain and computes the superimposed electric potential V(x, y)
using Coulomb's law:

    V = k·q / r

The electric field is recovered as E = −∇V via central differences
and displayed as a streamline plot.

Outputs (saved to outputs/):
  - electric_potential_3d.png   : 3-D surface of V(x, y)
  - electric_potential_contour.png : Equipotential contour lines
  - electric_field_streamplot.png  : Electric field streamlines
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Physical constants ───────────────────────────────────────────────────────
CHARGE_MAGNITUDE = 1.602176e-19          # elementary charge [C]
K_COULOMB        = 8.987e9               # Coulomb constant [N·m²/C²]

# ── Domain ───────────────────────────────────────────────────────────────────
DOMAIN_SIZE = 5.0
RESOLUTION  = 50

x = np.linspace(0, DOMAIN_SIZE, RESOLUTION)
y = np.linspace(0, DOMAIN_SIZE, RESOLUTION)
V = np.zeros((RESOLUTION, RESOLUTION))


# ── Charge class ─────────────────────────────────────────────────────────────
class PointCharge:
    """A positive point charge at a fixed position (xi, yi)."""

    def __init__(self, xi: float, yi: float, q: float = CHARGE_MAGNITUDE):
        self.x = xi
        self.y = yi
        self.q = q

    def potential(self, x_grid: np.ndarray, y_grid: np.ndarray) -> np.ndarray:
        """Compute the potential contribution on the (x_grid × y_grid) mesh.

        Avoids division by zero by skipping the singular point.
        """
        V_local = np.zeros((len(x_grid), len(y_grid)))
        for i, xi in enumerate(x_grid):
            for j, yj in enumerate(y_grid):
                r = np.sqrt((xi - self.x) ** 2 + (yj - self.y) ** 2)
                if r > 1e-9:
                    V_local[i, j] = K_COULOMB * self.q / r
        return V_local


# ── Place charges at the four corners ────────────────────────────────────────
charges = [
    PointCharge(0,           0          ),
    PointCharge(0,           DOMAIN_SIZE),
    PointCharge(DOMAIN_SIZE, 0          ),
    PointCharge(DOMAIN_SIZE, DOMAIN_SIZE),
]
for charge in charges:
    V += charge.potential(x, y)

X, Y = np.meshgrid(x, y)

# ── 1. 3-D surface plot ───────────────────────────────────────────────────────
fig = plt.figure(figsize=(9, 6))
ax  = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V.T, cmap='plasma', alpha=0.85)
ax.set_xlabel("x [m]"); ax.set_ylabel("y [m]"); ax.set_zlabel("V [V]")
ax.set_title("Electric Potential — 4 Corner Charges")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "electric_potential_3d.png"), dpi=150)
print("Saved outputs/electric_potential_3d.png")
plt.close()

# ── 2. Equipotential contour lines ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 6))
cs = ax.contourf(X, Y, V.T, levels=30, cmap='plasma')
plt.colorbar(cs, ax=ax, label="V [V]")
ax.contour(X, Y, V.T, levels=30, colors='white', linewidths=0.5, alpha=0.4)
ax.set_xlabel("x [m]"); ax.set_ylabel("y [m]")
ax.set_title("Equipotential Lines — 4 Corner Charges")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "electric_potential_contour.png"), dpi=150)
print("Saved outputs/electric_potential_contour.png")
plt.close()


# ── 3. Electric field via −∇V ────────────────────────────────────────────────
# np.gradient returns [dV/dy, dV/dx] for a 2-D array with spacing (dy, dx)
# V is stored as V[ix, iy], so gradient axis-0 = x, axis-1 = y
dV_dx, dV_dy = np.gradient(V, x, y)
Ex = -dV_dx.T   # E_x = -∂V/∂x  (transpose to match meshgrid orientation)
Ey = -dV_dy.T   # E_y = -∂V/∂y

speed = np.sqrt(Ex ** 2 + Ey ** 2)

fig, ax = plt.subplots(figsize=(7, 6))
strm = ax.streamplot(
    X, Y, Ex, Ey,
    color=speed, linewidth=1.5, cmap='autumn', density=1.5
)
plt.colorbar(strm.lines, ax=ax, label="|E| [V/m]")
ax.set_xlabel("x [m]"); ax.set_ylabel("y [m]")
ax.set_title("Electric Field Streamlines — 4 Corner Charges")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "electric_field_streamplot.png"), dpi=150)
print("Saved outputs/electric_field_streamplot.png")
plt.close()
