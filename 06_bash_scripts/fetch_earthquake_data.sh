#!/usr/bin/env bash
# fetch_earthquake_data.sh
# ──────────────────────────
# Downloads the seismic event dataset (sismos.txt) from GitHub,
# copies it to the physics simulations folder, and runs the
# earthquake map visualisation.
#
# Usage:
#   bash fetch_earthquake_data.sh

set -euo pipefail

SISMOS_URL="https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/sismos.txt"
SISMOS_FILE="sismos.txt"
SIM_DIR="$(dirname "$0")/../03_physics_simulations"

echo "Downloading $SISMOS_FILE ..."
wget -q "$SISMOS_URL" -O "$SIM_DIR/$SISMOS_FILE"

echo "Running earthquake map ..."
python3 "$SIM_DIR/earthquake_map.py"

echo "Done. Output saved to 03_physics_simulations/outputs/earthquake_map.png"
