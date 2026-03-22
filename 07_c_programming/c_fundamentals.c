/*
 * c_fundamentals.c
 * ─────────────────
 * A collection of standalone C exercises demonstrating:
 *   1. linspace()  — dynamically allocated linearly-spaced array
 *   2. file_io()   — writing integers to a text file
 *   3. geometry()  — computing sphere surface area in a loop
 *   4. arrays()    — static array initialisation and iteration
 *   5. dyn_array() — heap-allocated array with malloc / free
 *   6. cond_loop() — if/else and do-while constructs
 *
 * Compilation:
 *   cc c_fundamentals.c -lm -o c_fundamentals
 *
 * Run a specific exercise by uncommenting the desired call in main().
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846

/* Forward declarations */
void linspace(double start, double end, int n);
void file_io(void);
void geometry(void);
void arrays(void);
void dyn_array(void);
void cond_loop(void);


/* ── main ──────────────────────────────────────────────────────────────────── */
int main(void)
{
    linspace(0, 10, 10);
    /* Uncomment to run other exercises:
    file_io();
    geometry();
    arrays();
    dyn_array();
    cond_loop();
    */
    return 0;
}


/* ── 1. linspace ───────────────────────────────────────────────────────────── */
/*
 * Generates `n` evenly-spaced values in [start, end] using malloc,
 * prints them, then frees the allocated memory.
 */
void linspace(double start, double end, int n)
{
    int i;
    double *lista;
    double paso;

    if (n < 2) {
        fprintf(stderr, "linspace: n must be >= 2\n");
        return;
    }

    lista = (double *)malloc(n * sizeof(double));
    if (!lista) {
        fprintf(stderr, "linspace: malloc failed\n");
        exit(EXIT_FAILURE);
    }

    paso = (end - start) / (n - 1);
    for (i = 0; i < n; i++) {
        lista[i] = start + i * paso;
    }

    printf("linspace(%.1f, %.1f, %d):\n", start, end, n);
    for (i = 0; i < n; i++) {
        printf("  [%2d] %f\n", i, lista[i]);
    }

    free(lista);
}


/* ── 2. file_io ────────────────────────────────────────────────────────────── */
/*
 * Writes integers 0–9 to "output.dat", then reads and prints them back.
 */
void file_io(void)
{
    FILE *fp;
    int i, val;
    const char *filename = "output.dat";

    /* Write */
    fp = fopen(filename, "w");
    if (!fp) {
        fprintf(stderr, "file_io: cannot open %s for writing\n", filename);
        exit(EXIT_FAILURE);
    }
    for (i = 0; i < 10; i++) {
        fprintf(fp, "%d\n", i);
    }
    fclose(fp);

    /* Read back */
    fp = fopen(filename, "r");
    if (!fp) {
        fprintf(stderr, "file_io: cannot open %s for reading\n", filename);
        exit(EXIT_FAILURE);
    }
    printf("Contents of %s:\n", filename);
    while (fscanf(fp, "%d", &val) == 1) {
        printf("  %d\n", val);
    }
    fclose(fp);
}


/* ── 3. geometry ───────────────────────────────────────────────────────────── */
/*
 * Computes the surface area of a sphere  A = 4π r²
 * for integer radii 0–11 and prints a table.
 */
void geometry(void)
{
    int i;
    double radius, surface;

    printf("%-10s %-15s\n", "Radius", "Surface Area");
    printf("%-10s %-15s\n", "------", "------------");

    for (i = 0; i < 12; i++) {
        radius  = (double)i;
        surface = 4.0 * PI * radius * radius;
        printf("%-10.1f %-15.4f\n", radius, surface);
    }
}


/* ── 4. arrays ─────────────────────────────────────────────────────────────── */
/*
 * Demonstrates stack-allocated arrays: prints uninitialised values,
 * then initialises to even numbers and prints again.
 */
void arrays(void)
{
    int lista[10];
    int i;

    printf("Array before initialisation:\n");
    for (i = 0; i < 10; i++) {
        printf("  lista[%d] = %d\n", i, lista[i]);
    }

    for (i = 0; i < 10; i++) {
        lista[i] = i * 2;
    }

    printf("\nArray after initialisation (even numbers):\n");
    for (i = 0; i < 10; i++) {
        printf("  lista[%d] = %d\n", i, lista[i]);
    }
}


/* ── 5. dyn_array ──────────────────────────────────────────────────────────── */
/*
 * Heap-allocates an integer array with malloc, fills it with even numbers,
 * and releases memory with free.
 * NOTE: Intentional out-of-bounds access in the original was removed —
 *       accessing beyond allocated memory is undefined behaviour.
 */
void dyn_array(void)
{
    int i;
    int n_points = 10;
    int *arr;

    arr = (int *)malloc(n_points * sizeof(int));
    if (!arr) {
        fprintf(stderr, "dyn_array: malloc failed\n");
        exit(EXIT_FAILURE);
    }

    printf("Heap array at %p:\n", (void *)arr);
    for (i = 0; i < n_points; i++) {
        arr[i] = i * 2;
        printf("  arr[%d] = %d\n", i, arr[i]);
    }

    free(arr);
    printf("Memory freed.\n");
}


/* ── 6. cond_loop ──────────────────────────────────────────────────────────── */
/*
 * Demonstrates if/else comparisons and a do-while loop.
 */
void cond_loop(void)
{
    int a = 1, b = 2;

    /* if — a > b */
    if (a > b) {
        printf("a is greater than b: a=%d, b=%d\n", a, b);
    } else {
        printf("a is NOT greater than b: a=%d, b=%d\n", a, b);
    }

    /* if-else — a < b */
    a = 1; b = 1;
    if (a < b) {
        printf("a is less than b: a=%d, b=%d\n", a, b);
    } else {
        printf("a is equal to or greater than b: a=%d, b=%d\n", a, b);
    }

    /* do-while */
    printf("\ndo-while loop (a from 0 to 9):\n");
    a = 0; b = 10;
    do {
        printf("  a=%d\n", a);
        a++;
    } while (a < b);
}
