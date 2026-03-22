# 07 — C Programming

Introductory C exercises covering memory management, file I/O, arrays, and control flow.

---

## File

| File | Description | Original |
|------|-------------|----------|
| [c_fundamentals.c](c_fundamentals.c) | Six standalone exercises demonstrating C basics | `try.c` |

---

## Compilation & Running

```bash
cd 07_c_programming

# Compile (link math library with -lm)
cc c_fundamentals.c -lm -o c_fundamentals

# Run (executes whichever exercise is uncommented in main())
./c_fundamentals
```

To switch exercises, open `c_fundamentals.c`, comment/uncomment the desired function call in `main()`, and recompile.

---

## Exercises

### 1. `linspace(start, end, n)`
Generates n linearly-spaced `double` values in the range [start, end].
Uses `malloc` for the array and `free` to release it.

**Sample output:**
```
linspace(0.0, 10.0, 10):
  [ 0] 0.000000
  [ 1] 1.111111
  ...
  [ 9] 10.000000
```

### 2. `file_io()`
Writes integers 0–9 to `output.dat` with `fprintf`, then reads them back with `fscanf`.

### 3. `geometry()`
Prints a table of sphere surface areas `A = 4πr²` for radius = 0…11.

### 4. `arrays()`
Demonstrates stack-allocated arrays: prints uninitialised values, then fills with even numbers (0, 2, 4, …).

### 5. `dyn_array()`
Allocates an integer array on the heap with `malloc`, fills it, prints each element, and frees with `free`.

### 6. `cond_loop()`
Shows `if/else` branches and a `do-while` countdown loop.

---

## Key Concepts

| Concept | C Construct | Notes |
|---------|-------------|-------|
| Heap allocation | `malloc(n * sizeof(type))` | Must be paired with `free()` |
| Memory safety | `if (!ptr) { exit(FAILURE); }` | Always check malloc return |
| Math functions | `#include <math.h>`, link `-lm` | `pow()`, `sqrt()`, etc. |
| Formatted I/O | `printf("%f\n", val)` | `%d`=int, `%f`=float/double |
| File I/O | `fopen` / `fprintf` / `fclose` | Always close files |

---

## Improvements Over Original Code

| Issue | Fix |
|-------|-----|
| `for(i=0; ...)` — `i` undeclared in `hacerlinea` | Declared `int i;` at top of function |
| `malloc(n * sizeof(int))` for a `float` array | Changed allocation to `sizeof(double)` |
| Missing semicolon in `fprintf(in, "%d\n",i)` | Added semicolon |
| Out-of-bounds write `array_int[n_points*10000]` (undefined behaviour) | Removed; added safety note |
| Functions declared without forward declarations | Added prototypes before `main()` |
| `#define PI 3.13159` (wrong value) | Corrected to `3.14159265358979323846` |
| Volume formula used surface variable (incorrect) | Fixed: `surface = 4πr²` |
| No `free()` calls after `malloc` | Added `free()` at end of each function |
