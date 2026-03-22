"""
Dictionaries and Control Flow in Python
=========================================
Covers dictionary creation, iteration, and deletion;
conditional statements; for/while loops; break, continue,
and else clauses with loops.
"""

# ── 1. Dictionary Basics ────────────────────────────────────────────────────
print("=== 1. Creating dictionaries ===")

# Method 1: empty dict + assignment
phonebook = {}
phonebook["John"] = 1235474
phonebook["Jack"] = 5465423
phonebook["Jill"] = 4654645
print(phonebook)

# Method 2: literal syntax
phonebook = {"John": 1235474, "Jack": 5465423, "Jill": 4654645}
print(phonebook)

# ── 2. Iterating Over a Dictionary ─────────────────────────────────────────
print("\n=== 2. Iterating with .items() ===")
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# ── 3. Adding and Deleting Entries ──────────────────────────────────────────
print("\n=== 3. Adding and deleting entries ===")
phonebook = {"John": 1235474, "Jack": 5465423, "Jill": 4654645}
del phonebook["John"]
phonebook["Juanito"] = 1235474
print(phonebook)

# ── 4. Dictionary Exercise ──────────────────────────────────────────────────
print("\n=== 4. Exercise: add Jake, remove Jill ===")
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
phonebook["Jake"] = 938273443
del phonebook["Jill"]
print(phonebook)

# ── 5. Conditional Statements ───────────────────────────────────────────────
print("\n=== 5. Conditionals ===")
number       = 16
second_number = 0
first_array  = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1 — number > 15")
if first_array:
    print("2 — first_array is non-empty")
if len(second_array) == 2:
    print("3 — second_array has 2 elements")
if len(first_array) + len(second_array) == 5:
    print("4 — combined length is 5")
if first_array and first_array[0] == 1:
    print("5 — first element is 1")
if not second_number:
    print("6 — second_number is falsy (0)")

# ── 6. For Loops ────────────────────────────────────────────────────────────
print("\n=== 6. For loops ===")
primes = [2, 3, 5, 7]
for p in primes:
    print(p)

print("range(5):", list(range(5)))
print("range(3,6):", list(range(3, 6)))
print("range(3,8,2):", list(range(3, 8, 2)))

# ── 7. While Loop ───────────────────────────────────────────────────────────
print("\n=== 7. While loop ===")
count = 0
while count < 5:
    print(count)
    count += 1

# ── 8. Break and Continue ───────────────────────────────────────────────────
print("\n=== 8. Break and continue ===")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("Odd numbers 0-9 (using continue):")
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# ── 9. Else Clauses on Loops ────────────────────────────────────────────────
print("\n=== 9. Else on loops ===")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("while finished — count reached %d" % count)

# for-else: else runs only if loop was NOT broken
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("This is not printed because break was hit")

# ── 10. Exercise: Find 237 in a Number List ─────────────────────────────────
print("\n=== 10. Exercise: find 237 and print even numbers before it ===")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105,
    942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
    615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
    626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,
    843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857,
    440, 380, 126, 721, 328, 753, 470, 743, 527
]

print("Even numbers up to (and excluding) 237:")
for number in numbers:
    if number % 2 == 0:
        print(number)
    if number == 237:
        break
