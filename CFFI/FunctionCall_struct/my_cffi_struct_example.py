# my_cffi_struct_example.py
from cffi import FFI

# Create an FFI object
ffi = FFI()

# Load the shared library (assuming the compiled C code is in 'example.so' or 'example.dll')
# Replace 'example' with the actual name of your compiled C library.
example = ffi.dlopen('./example.so')  # On Windows, use '.dll' instead of '.so'

# Define the struct in cdef
ffi.cdef("struct foo_s { int a, b; };")

# Call the C function that returns a struct
myfoo = example.function_returning_a_struct()

# Access and print the struct's members
print(f"myfoo.a: {myfoo.a}")
print(f"myfoo.b: {myfoo.b}")

