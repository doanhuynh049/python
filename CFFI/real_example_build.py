from cffi import FFI
ffi = FFI()

ffi.set_source("real_simple_example",
    """ // passed to the real C compiler
    #include <sys/types.h>
    #include <pwd.h>
    """,
    libraries=[])
ffi.cdef("""
    struct passwd {
        char *pw_name;
        ...; // literally dot-dot-dot
    };
    struct passwd *getpwuid(int uid);
""")

if __name__ == "__main__":
    ffi.compile()
