"""
Greatest Common Divisor (GCD) Calculator
==========================================
Accepts two integers A and B from the user and:
  1. Determines whether A is even or odd.
  2. Lists all positive divisors of A and B.
  3. Finds the GCD by comparing the two divisor sets.

This is a pedagogical implementation; Python's built-in
math.gcd() provides the same result more efficiently.
"""

import math


def get_divisors(n: int) -> list:
    """Return a sorted list of all positive divisors of n."""
    return [d for d in range(1, abs(n) + 1) if n % d == 0]


def find_gcd(a: int, b: int) -> int:
    """Find GCD by intersecting divisor lists (educational approach)."""
    div_a = get_divisors(a)
    div_b = get_divisors(b)
    common = set(div_a) & set(div_b)
    return max(common)


# ── User input ───────────────────────────────────────────────────────────────
try:
    A = int(input("Enter integer A: "))
    B = int(input("Enter integer B: "))
except ValueError:
    print("Please enter valid integers.")
    raise SystemExit(1)

print(f"\nA = {A},  B = {B}")

# ── Even / odd ───────────────────────────────────────────────────────────────
parity = "even" if A % 2 == 0 else "odd"
print(f"A is {parity}.")

# ── Divisors ─────────────────────────────────────────────────────────────────
div_A = get_divisors(A)
div_B = get_divisors(B)
print(f"\nDivisors of A ({A}): {div_A}")
print(f"Divisors of B ({B}): {div_B}")

# ── GCD ──────────────────────────────────────────────────────────────────────
gcd = find_gcd(A, B)
print(f"\nGCD({A}, {B}) = {gcd}")

# Verify against built-in
assert gcd == math.gcd(abs(A), abs(B)), "Mismatch with math.gcd — check logic!"
print("(Verified against math.gcd ✓)")
