# file "simple_example_build.py"
from cffi import FFI

ffi = FFI()
ffi.set_source("_simple_example", None)
ffi.cdef("""
    int printf(const char *format, ...);
""")

if __name__ == "__main__":
    ffi.compile()

