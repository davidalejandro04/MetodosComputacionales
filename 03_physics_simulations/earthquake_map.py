"""
Earthquake Epicentre Map
=========================
Reads latitude and longitude coordinates from a seismic event
dataset (sismos.txt) and plots the geographic distribution of
earthquake epicentres as a scatter map.

The data file is downloaded from:
  https://raw.githubusercontent.com/ComputoCienciasUniandes/
  MetodosComputacionalesDatos/master/hands_on/sismos.txt

Run the fetch script in 06_bash_scripts/fetch_earthquake_data.sh
to download sismos.txt before executing this file.

Output saved to outputs/earthquake_map.png.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

DATA_FILE = os.path.join(os.path.dirname(__file__), "sismos.txt")

# ── Load data ────────────────────────────────────────────────────────────────
if not os.path.exists(DATA_FILE):
    print("ERROR: sismos.txt not found.")
    print("Run '06_bash_scripts/fetch_earthquake_data.sh' to download it.")
    sys.exit(1)

latitude  = np.genfromtxt(DATA_FILE, delimiter="\t", skip_header=1, usecols=20)
longitude = np.genfromtxt(DATA_FILE, delimiter="\t", skip_header=1, usecols=21)

# Remove NaN rows (incomplete records)
mask      = np.isfinite(latitude) & np.isfinite(longitude)
latitude  = latitude[mask]
longitude = longitude[mask]

print(f"Loaded {len(latitude)} earthquake records.")

# ── Plot ─────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 7))

scatter = ax.scatter(
    longitude, latitude,
    s=8, c='crimson', alpha=0.4, edgecolors='none',
    label=f"Epicentres (n={len(latitude)})"
)

ax.set_xlabel("Longitude [°]", fontsize=12)
ax.set_ylabel("Latitude [°]",  fontsize=12)
ax.set_title("Seismic Epicentre Distribution", fontsize=14)
ax.legend(markerscale=3)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "earthquake_map.png"), dpi=150)
print("Saved outputs/earthquake_map.png")
plt.close()
