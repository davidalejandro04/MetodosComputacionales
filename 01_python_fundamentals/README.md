# 01 — Python Fundamentals

Introduction to Python programming covering data structures, control flow, file I/O, NumPy arrays, and object-oriented programming.

---

## Files

| File | Description | Original |
|------|-------------|----------|
| [lists_and_operators.py](lists_and_operators.py) | List creation, indexing, concatenation, arithmetic & string operators | `Clase2_1.py` |
| [dicts_and_control_flow.py](dicts_and_control_flow.py) | Dictionaries, conditionals, for/while loops, break/continue | `Clase2_2.py` |
| [file_io_and_parsing.py](file_io_and_parsing.py) | Reading a text file, extracting and parsing structured fields | `Clase3_1.py` |
| [numpy_and_functions.py](numpy_and_functions.py) | NumPy arrays, BMI/unit conversion, defining and calling functions | `Clase3_2.py` |
| [classes_and_oop.py](classes_and_oop.py) | Class definition, constructor, instance methods, BMI calculator | `Clase4_1.py` |
| [greeter.py](greeter.py) | Minimal demo of a function that accepts arguments | `recibir.py` |

---

## Running

```bash
# Each file is self-contained — run with Python 3
python lists_and_operators.py
python dicts_and_control_flow.py
python classes_and_oop.py

# file_io_and_parsing.py requires the contact data file
# (download it first with the bash script in 06_bash_scripts)
python file_io_and_parsing.py

# numpy_and_functions.py and greeter.py ask for interactive input
python numpy_and_functions.py
python greeter.py
```

---

## Concepts Covered

### `lists_and_operators.py`
- `list.append()`, zero-based indexing, iteration
- Arithmetic operators: `+`, `-`, `*`, `/`, `**`, `%`
- String repetition and list concatenation
- `%`-style string formatting

### `dicts_and_control_flow.py`
- Dictionary literal and dynamic creation
- `dict.items()` for iteration; `del` for removal
- `if / elif / else` conditions
- `for` with `range()`; `while` with `count`
- `break` and `continue`; `else` clause on loops

### `file_io_and_parsing.py`
- `open()` / `readlines()` / `close()`
- `str.rstrip('\n')` to strip newlines
- `str.split()` and `str.split(',')` for tokenising

### `numpy_and_functions.py`
- `np.array()` from a Python list
- Vectorised operations (BMI formula, kg → lbs conversion)
- Boolean masking: `arr[arr > threshold]`
- `def` with positional arguments; `return` statements

### `classes_and_oop.py`
- `class` definition with `__init__` constructor
- Instance attributes (`self.name`, `self.weight`, …)
- Methods with `self` parameter; optional return types
- Type hints (`str`, `float`) and docstrings

---

## Sample Output

### `lists_and_operators.py`
```
=== 1. Creating and appending to a list ===
[1, 2, 3]
1
2
3
...
x_list contains 10 objects
y_list contains 10 objects
big_list contains 20 objects
Almost there...
Great!
```

### `classes_and_oop.py`
```
Weight in kg : 113.4
Weight in lbs: 249.48
Height (m)   : 2.06
Player: LeBron James | Weight: 113.4 kg (249.5 lbs) | Height: 2.06 m | BMI: 26.7
Player: Stephen Curry | Weight: 84.0 kg (184.8 lbs) | Height: 1.88 m | BMI: 23.8
```

---

## Improvements Over Original Code

| Issue | Fix |
|-------|-----|
| `raw_input()` (Python 2) | Replaced with `input()` (Python 3) |
| `print x` bare statements | Replaced with `print(x)` function calls |
| Missing colons after `def` in `Clase4_1.py` | Added colons and corrected indentation |
| `self.name` referenced but never set | Fixed: `__init__` now sets `self.name` |
| No constructor parameters | Full `__init__(name, weight, height)` added |
| Spelling: `unidad` logic missing `else` colon | Fixed with `elif` / `else` chain |
