# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 02:08:55 2017

@author: Dimitar Nikolov
"""

# This program uses the Newton-Raphson formula for guessing the square root of a number.

epsilon = 0.01
y = float(input("Enter a number: "))
guess = y / 2.0
numberOfGuesses = 0

while abs(guess * guess - y) >= epsilon:
    numberOfGuesses += 1
    guess = guess - (((guess ** 2) - y)/(2 * guess))
print("The number of guesses required was ", str(numberOfGuesses))
print("The square root of", str(y), "is about", str(guess))