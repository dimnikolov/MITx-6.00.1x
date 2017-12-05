# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 01:40:30 2017

@author: Dimitar Nikolov
"""

# This Python program asks the user to guess a number between 0 and 100.
# It guesses the number by asking the user to give input if the guesses
# that it makes are low, high, or, in the case of a correct guess, right.

low = 0
high = 100
answer = False

while answer != True:
    guess = int((low + high) / 2)
    print("Please think of a number between 0 and 100!")
    print("Is your number", str(guess), "?", end="")
    user_input = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    
    if user_input == "h":
        high = guess
        
    elif user_input == "l":
        low = guess
        
    elif user_input == "c":
        print("Game over. Your secret number was:", str(guess))
        answer = True
        
    else:
        print("Sorry, I did not understand your input.")
        continue
