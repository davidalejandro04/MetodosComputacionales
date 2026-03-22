# 06 — Bash Scripts

Shell scripts that automate data acquisition and trigger the Python analysis pipelines. Each script downloads its required dataset, runs the relevant Python module, and cleans up temporary files.

---

## Files

| Script | Description | Original |
|--------|-------------|----------|
| [fetch_word_frequency_data.sh](fetch_word_frequency_data.sh) | Download Romeo & Juliet from Gutenberg, run word-frequency analysis | `ej2labw1.sh` |
| [fetch_contact_data.sh](fetch_contact_data.sh) | Download sample contact file, run file I/O parsing exercise | `ejercicio2.sh` |
| [fetch_earthquake_data.sh](fetch_earthquake_data.sh) | Download seismic dataset (sismos.txt), run earthquake map | `ejercicioSismos.sh` |
| [engineering_pass_rate.sh](engineering_pass_rate.sh) | Count Engineering students passing with average ≥ 3.0 | `ingenieria.sh` |
| [math_pass_rate.sh](math_pass_rate.sh) | Count Mathematics students passing with average ≥ 3.0 | `matematicas.sh` |

---

## Running

```bash
# Make executable (Linux/macOS)
chmod +x 06_bash_scripts/*.sh

# Then run individually:
bash 06_bash_scripts/fetch_word_frequency_data.sh
bash 06_bash_scripts/fetch_earthquake_data.sh
bash 06_bash_scripts/engineering_pass_rate.sh
bash 06_bash_scripts/math_pass_rate.sh
```

> **Windows users**: Run these inside Git Bash, WSL, or Cygwin.

---

## Concepts Covered

### `wget`
Downloads a remote file to disk:
```bash
wget -q "https://example.com/data.txt" -O "local_name.txt"
```

### `awk`
Pattern-matching and field-processing tool for structured text:
```bash
# Print field $1 if programme ($3) starts with "ING" and average ≥ 3
awk 'substr($3,1,3)=="ING" && ($4+$5+$6)/3>=3 {print $1}' data.tsv
```

### `wc -l`
Counts lines in a stream, used here to count matching students:
```bash
awk '...' data.tsv | wc -l > result.txt
```

### `set -euo pipefail`
Robust error handling:
- `-e`: Exit immediately on non-zero return code
- `-u`: Treat unset variables as errors
- `-o pipefail`: Propagate errors through pipelines

---

## Improvements Over Original Code

| Issue | Fix |
|-------|-----|
| No shebang line | Added `#!/usr/bin/env bash` |
| No error handling | Added `set -euo pipefail` |
| Hard-coded file names | Variables with descriptive names |
| References to old file names (`ej2labw1.py`, etc.) | Updated to reference new module paths |
| Silence — no progress output | Added `echo` status messages |
| `python` command (version ambiguous) | Changed to `python3` |
