import os
cwd = os.getcwd()
import sys
sys.path.append(cwd)

from pathlib import Path
path = Path(cwd)
a = str(path.parent.absolute())

sys.path.append(a)

# Importing the basic_operations module from the python_introduction package
from python_introduction import basic_operations
print(basic_operations.add(5, 3))
print(basic_operations.subtract(5, 3))
print(basic_operations.multiply(5, 3))
print(basic_operations.divide(5, 3))