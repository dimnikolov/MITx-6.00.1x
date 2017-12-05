# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:15:46 2017

@author: Dimitar Nikolov
"""

# This Python program guesses the square root using bisection search.

x = 100
low = 0
high = x
epsilon = 0.01
guess_count = 0
answer = (high + low)/2.0

while abs(answer**2 - x) >= epsilon:
    print("low = " + str(low) + "\n high = " + str(high) + "\n  answer = " + str(answer) + "\n")
    guess_count += 1
    
    if answer**2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low)/2.0
print("guess_count = " + str(guess_count))
print(str(answer) + "is close to the square root of " + str(x))
    