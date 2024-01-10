from real_simple_example import ffi, lib

# Call getpwuid(0) and store the result in the variable 'p'
p = lib.getpwuid(0)

# Display the value of 'p.pw_name' using ffi.string()
pw_name_bytes = ffi.string(p.pw_name)
print(f"pw_name_bytes: {pw_name_bytes}")

# Check if 'pw_name_bytes' is equal to b'root' and print the result
assert pw_name_bytes == b'root'

# Print a message indicating that the assertion passed
print("Assertion passed: pw_name_bytes is 'root'")


