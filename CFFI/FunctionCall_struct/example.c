// example.c
#include <stdio.h>

// Define a simple struct
struct foo_s {
    int a;
    int b;
};

// Function that returns a struct
struct foo_s function_returning_a_struct() {
    struct foo_s result;
    result.a = 42;
    result.b = 84;
    return result;
}

