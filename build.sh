#!/bin/bash

python setup.py build_ext --inplace || exit 1
pyinstaller hello.spec || exit 1