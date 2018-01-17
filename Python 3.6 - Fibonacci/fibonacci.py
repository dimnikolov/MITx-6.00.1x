def fib(x):
    """
    Assumes x is an int >= 0
    Returns Fibonacci number of x
    """
    
    if x == 0 or x == 1:
        return 1
    else:
        fibonacci = fib(x-1) + fib(x-2)
        return fibonacci
        