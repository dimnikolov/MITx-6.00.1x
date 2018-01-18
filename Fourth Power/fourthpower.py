def fourthpower(x):
    """
    Inputs x. Takes x to the fourth (4th) power.
    It does so using a function inside a function -- secondpower(x).
    This is an exercise in using functions and scopes/namespaces.
    """
    def secondpower(x):
        x = x ** 2
    
    secondpower(secondpower(x))