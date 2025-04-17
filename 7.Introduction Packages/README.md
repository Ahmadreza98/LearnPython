## Packages and Modules in Python

---
### 1. MODULE in Python
A module is just a single Python file (`.py`) that contains 
variables, functions, classes, etc.
```
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```
Now you can use it in another Python file:
```
import math_utils

print(math_utils.add(5, 3))  # Output: 8
```
You can also do:
```
from math_utils import add
print(add(2, 2))  # Output: 4
```
### 2. PACKAGE in Python
A package is a collection of modules organized in a folder — it 
must contain a special file called `__init__`.py (even if it’s empty).
```
my_package/
├── __init__.py
├── math_utils.py
└── string_utils.py
```
Now you can use it like:
```
from my_package import math_utils
print(math_utils.add(10, 20))
```
```
from my_package.math_utils import add
print(add(1, 1))
```
### 3. Built-in & External Module
- **Built-in modules**: Python comes with modules like `math`, `random`, 
  `os`, `datetime`, etc.
- **External packages**: You can install packages via `pip`, like:
```
pip install numpy
```
Then:
```
import numpy as np
```