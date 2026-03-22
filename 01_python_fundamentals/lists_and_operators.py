"""
Lists and Basic Operators in Python
====================================
Demonstrates Python list creation, manipulation, indexing,
concatenation, and basic arithmetic/string operators.
"""

# ── 1. List Creation & Appending ────────────────────────────────────────────
print("=== 1. Creating and appending to a list ===")
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)            # [1, 2, 3]
print(my_list[0])         # 1 (zero-based index)
print(my_list[1])         # 2
print(my_list[2])         # 3

print("\nIterating over the list:")
for x in my_list:
    print(x)

# ── 2. Indexing ──────────────────────────────────────────────────────────────
print("\n=== 2. Accessing elements by index ===")
my_list = [1, 2, 3]
print(my_list[1])         # 2

# ── 3. Mixed Lists & Second Element ─────────────────────────────────────────
print("\n=== 3. Mixed lists ===")
numbers = [1, 2, 3]
strings = ["numbers", "hello", "world"]
names   = ["John", "Eric", "Jessica"]

second_name = names[1]

print(numbers)
print(strings)
print("Second name:", second_name)

# ── 4. Basic Arithmetic Operators ────────────────────────────────────────────
print("\n=== 4. Arithmetic operators ===")
number    = 1 + 2 * 3 / 4.0   # operator precedence: * and / before +
remainder = 11 % 3             # modulo
squared   = 7 ** 2             # exponentiation
cubed     = 2 ** 3

print("1 + 2*3/4.0 =", number)
print("11 % 3 =", remainder)
print("7² =", squared, "  2³ =", cubed)

# ── 5. String Repetition & List Concatenation ────────────────────────────────
print("\n=== 5. Repetition and concatenation ===")
lots_of_hellos = "hello" * 10
print(lots_of_hellos)

even_numbers = [2, 4, 6, 8]
odd_numbers  = [1, 3, 5, 7]
all_numbers  = odd_numbers + even_numbers
print("All numbers:", all_numbers)
print([1, 2, 3] * 3)

# ── 6. Final Exercise: Object Lists ─────────────────────────────────────────
print("\n=== 6. Final exercise: counting objects in lists ===")
x = object()
y = object()

x_list   = [x] * 10
y_list   = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# ── 7. String Formatting Reference ──────────────────────────────────────────
print("\n=== 7. String formatting examples ===")
# %s  → string    %d → integer    %f → float
# %.<digits>f → fixed decimal     %x/%X → hex
print("Name: %s, Age: %d, Score: %.2f" % ("Alice", 22, 9.876))
print("Hex: %x / %X" % (255, 255))
