"""
This is a script for multiplication in Python through an iterative solution.
It is based on the principle that "Multiply a * b" is equivalent to "Add a to itself b times"
"""

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    print('The result is', result)
    return result

mult_iter(3,5)