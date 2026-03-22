#!/usr/bin/env bash
# engineering_pass_rate.sh
# ─────────────────────────
# Downloads the student grades TSV file and counts how many
# Engineering (ING) students achieved an average grade ≥ 3.0
# across their three exam scores.
#
# Output written to: pasaroning.txt
#
# Usage:
#   bash engineering_pass_rate.sh

set -euo pipefail

GRADES_URL="https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv"
GRADES_FILE="01_notas.tsv"
OUTPUT_FILE="pasaroning.txt"

echo "Downloading grades file ..."
wget -q "$GRADES_URL" -O "$GRADES_FILE"

echo "Counting Engineering students with average ≥ 3.0 ..."
# Fields: $1=ID  $2=Name  $3=Programme  $4,$5,$6=Exam scores
# Filter: programme starts with "ING" AND (score1+score2+score3)/3 >= 3.0
count=$(awk 'substr($3,1,3)=="ING" && ($4+$5+$6)/3>=3 {print $1}' "$GRADES_FILE" | wc -l)

{
    echo "$count"
    echo "Engineering students passed (average ≥ 3.0)"
} > "$OUTPUT_FILE"

cat "$OUTPUT_FILE"

echo "Cleaning up ..."
rm -f "$GRADES_FILE"

echo "Done. Results written to $OUTPUT_FILE"
