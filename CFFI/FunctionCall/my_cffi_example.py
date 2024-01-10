# my_cffi_example.py
from cffi import FFI

# Create an FFI object
ffi = FFI()

# Load the shared library (assuming the compiled C code is in 'example.so' or 'example.dll')
# Replace 'example' with the actual name of your compiled C library.
example = ffi.dlopen('./example.so')  # On Windows, use '.dll' instead of '.so'

# Define the C function signature
ffi.cdef("int add(int a, int b);")

# Call the C function
result = example.add(5, 3)

# Print the result
print(f"The result of adding 5 and 3 is: {result}")

