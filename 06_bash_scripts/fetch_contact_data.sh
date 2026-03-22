#!/usr/bin/env bash
# fetch_contact_data.sh
# ──────────────────────
# Downloads a sample contact text file and runs the file I/O
# parsing exercise (01_python_fundamentals/file_io_and_parsing.py).
# Removes the downloaded file afterwards.
#
# Usage:
#   bash fetch_contact_data.sh

set -euo pipefail

CONTACT_URL="https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionales/master/hands_on/python/contacto_de_JaimeForero.txt"
CONTACT_FILE="contacto_de_JaimeForero.txt"
SCRIPT_DIR="$(dirname "$0")/../01_python_fundamentals"
SCRIPT="$SCRIPT_DIR/file_io_and_parsing.py"

echo "Downloading $CONTACT_FILE ..."
wget -q "$CONTACT_URL" -O "$CONTACT_FILE"

echo "Running file I/O parsing exercise ..."
# Run from the fundamentals directory so the script finds the file
(cd "$SCRIPT_DIR" && cp "$(pwd)/../../06_bash_scripts/$CONTACT_FILE" . && python3 file_io_and_parsing.py && rm -f "$CONTACT_FILE")

echo "Cleaning up ..."
rm -f "$CONTACT_FILE"

echo "Done."
