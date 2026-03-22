"""
Word-Length Frequency Analysis
================================
Reads a plain-text file (Project Gutenberg: Romeo & Juliet, pg1524.txt),
tokenises it into words, counts how many words have each length
from 1 to 20 characters, and plots the frequency distribution.

The text file is downloaded by 06_bash_scripts/fetch_word_frequency_data.sh.

Output saved to outputs/word_frequency.png.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

TEXT_FILE = os.path.join(os.path.dirname(__file__), "pg1524.txt")

# ── Load and tokenise ────────────────────────────────────────────────────────
if not os.path.exists(TEXT_FILE):
    print("ERROR: pg1524.txt not found.")
    print("Run '06_bash_scripts/fetch_word_frequency_data.sh' to download it.")
    sys.exit(1)

with open(TEXT_FILE, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Flatten all lines into a single list of whitespace-delimited tokens
words = [word for line in lines[1:] for word in line.split()]
total_words = len(words)
print(f"Total tokens: {total_words:,}")

# ── Count words by length ─────────────────────────────────────────────────────
MAX_LEN = 20
lengths    = list(range(1, MAX_LEN + 1))
counts     = []

for length in lengths:
    count = sum(1 for w in words if len(w) == length)
    counts.append(count)
    print(f"  Length {length:2d}: {count:6,} words")

# ── Plot ─────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(lengths, counts, color='steelblue', edgecolor='white', alpha=0.85)
ax.set_xlabel("Word Length (characters)")
ax.set_ylabel("Frequency")
ax.set_title("Word-Length Frequency Distribution\n(Romeo & Juliet — Project Gutenberg)")
ax.set_xticks(lengths)
ax.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "word_frequency.png"), dpi=150)
print("\nSaved outputs/word_frequency.png")
plt.close()
