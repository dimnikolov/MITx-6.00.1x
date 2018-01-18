"""

This is a recursive solution for multiplication.

"""

def mult(a, b):
    if b == 1:
        result = a
        print("The result is:", result)
        return a
    else:
        result = a + mult(a, b-1)
        print("The result is:", result)
        return result
    
mult(5, 1)