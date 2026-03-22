"""
NumPy Arrays and Functions in Python
=======================================
Covers:
  - NumPy array creation from Python lists
  - Vectorised arithmetic (BMI calculation, unit conversion)
  - Boolean array filtering
  - Defining and calling functions with arguments
  - Returning values from functions and building sentences
"""

import numpy as np

# ── 1. Find even numbers until 237 (warm-up loop review) ────────────────────
print("=== 1. Even numbers up to 237 ===")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105,
    942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
    615, 953, 345, 399, 162, 758, 219, 918, 237,
]
for n in numbers:
    if n % 2 == 0:
        print(n)
    if n == 237:
        break

# ── 2. NumPy Arrays and BMI ──────────────────────────────────────────────────
print("\n=== 2. NumPy arrays — BMI calculation ===")
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print("BMI values:", bmi)
print("BMI > 23 mask:", bmi > 23)
print("BMI values > 23:", bmi[bmi > 23])

# ── 3. Unit Conversion ───────────────────────────────────────────────────────
print("\n=== 3. Weight conversion: kg → lbs ===")
weight_kg    = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2
print("lbs:", np_weight_lbs)

# ── 4. Functions with Arguments ─────────────────────────────────────────────
print("\n=== 4. Functions with arguments ===")
nombre = input("What is your name? ")

def greet(username, greeting):
    """Print a personalised greeting."""
    print("Hello, %s — %s" % (username, greeting))
    print("The following are benefits of using functions:")

greet(nombre, "welcome!")

# ── 5. Return Values and Sentence Building ───────────────────────────────────
print("\n=== 5. Functions that return values ===")

def list_benefits():
    """Return a list of function benefits."""
    return [
        "More organised code ",
        "More readable code ",
        "Easier code reuse ",
        "Allowing programmers to share and connect code together ",
    ]

def build_sentence(benefit):
    """Append a fixed suffix to a benefit string."""
    return benefit + "is a benefit of functions!"

def name_the_benefits_of_functions():
    """Print every benefit as a complete sentence."""
    for benefit in list_benefits():
        print(build_sentence(benefit))

name_the_benefits_of_functions()
