# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:25:52 2017

@author: Dimitar Nikolov
"""

# This script uses the Guess and Check pattern in Python to find the cube root
# of 27 (the answer is 3, as 3 * 3 = 9 * 3 = 27).

# Guess and check the cube root of 27.
cube = 27
# epsilon means how close, in numerical value, we want to get to the answer.
# The bigger the value of epsilon, the faster (and less accurate) the answer.
# The smaller the value of epsilon, the slower (and more accurate) the answer.
epsilon = 0.01 
# start_at is our starting value.
guess = 0.0 
# The size in which to increase the guess as the check continues.
increment_by = 0.0001 
# Keep track of how many times we have gone through the loop.
number_of_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    guess += increment_by # This is short syntax for guess = guess + increment_by
    number_of_guesses += 1 # Increase the number of guesses value by 1
print('Number of guesses =', number_of_guesses)

if abs(guess**3 - cube) >= epsilon:
    print('Failed on the cube root of', cube) # Let's store cube as a variable, and not as 27. 
    # Doing so will enable me to make a next version of this script that supports user input 
    # for the value of cube, and not just the hardcoded value of 27.
else:
    print(guess, 'is close to the cube root of', cube)