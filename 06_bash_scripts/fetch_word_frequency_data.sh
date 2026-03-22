#!/usr/bin/env bash
# fetch_word_frequency_data.sh
# ─────────────────────────────
# Downloads "Romeo and Juliet" from Project Gutenberg, runs the
# word-frequency analysis, and removes the downloaded text file.
#
# Usage:
#   bash fetch_word_frequency_data.sh

set -euo pipefail

TEXT_URL="http://www.gutenberg.org/cache/epub/1524/pg1524.txt"
TEXT_FILE="pg1524.txt"
SCRIPT="$(dirname "$0")/../04_data_analysis/word_frequency.py"

echo "Downloading $TEXT_FILE ..."
wget -q "$TEXT_URL" -O "$TEXT_FILE"

echo "Running word frequency analysis ..."
python3 "$SCRIPT"

echo "Cleaning up ..."
rm -f "$TEXT_FILE"

echo "Done. Output saved to 04_data_analysis/outputs/word_frequency.png"
