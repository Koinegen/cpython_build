from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["src/logic/super_secret_library.py", "src/gateway/gateway.py"])
)
