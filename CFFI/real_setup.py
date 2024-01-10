from setuptools import setup

setup(
    name="YourPackage",  # Replace with the name of your package
    version="1.0.0",  # Replace with the version number
    description="Your package description",  # Replace with the package description
    author="Your Name",  # Replace with your name
    author_email="your@email.com",  # Replace with your email
    url="https://github.com/yourusername/yourpackage",  # Replace with your package's URL
    # Add other package metadata as needed
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["real_example_build.py:ffi"],
    install_requires=["cffi>=1.0.0"],
)
