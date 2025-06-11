import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Importing the basic_operations module from the python_introduction package
from python_introduction import basic_operations
print(basic_operations.add(5, 3))
print(basic_operations.subtract(5, 3))
print(basic_operations.multiply(5, 3))
print(basic_operations.divide(5, 3))