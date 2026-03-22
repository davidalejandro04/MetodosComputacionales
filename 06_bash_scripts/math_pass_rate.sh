#!/usr/bin/env bash
# math_pass_rate.sh
# ──────────────────
# Downloads the student grades TSV file and counts how many
# Mathematics (MATEMA) students achieved an average grade ≥ 3.0
# across their three exam scores.
#
# Output written to: pasaron.txt
#
# Usage:
#   bash math_pass_rate.sh

set -euo pipefail

GRADES_URL="https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv"
GRADES_FILE="01_notas.tsv"
OUTPUT_FILE="pasaron.txt"

echo "Downloading grades file ..."
wget -q "$GRADES_URL" -O "$GRADES_FILE"

echo "Counting Mathematics students with average ≥ 3.0 ..."
# Fields: $1=ID  $2=Name  $3=Programme  $4,$5,$6=Exam scores
# Filter: programme == "MATEMA" AND (score1+score2+score3)/3 >= 3.0
count=$(awk '$3=="MATEMA" && ($4+$5+$6)/3>=3 {print $1}' "$GRADES_FILE" | wc -l)

{
    echo "$count"
    echo "Mathematics students passed (average ≥ 3.0)"
} > "$OUTPUT_FILE"

cat "$OUTPUT_FILE"

echo "Cleaning up ..."
rm -f "$GRADES_FILE"

echo "Done. Results written to $OUTPUT_FILE"
