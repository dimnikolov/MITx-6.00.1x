# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:59:34 2017

@author: Dimitar Nikolov
"""

# This is Iteration 3, or the second refactoring of my Zen of Python script.
# This is by far my cleanest attempt at storing and printing the poem. How it works:
# The poem is stored in a text file called Poem.txt. Then, a function called zenOfPython
# reads the file -- and prints its contents. Simple! This separates the content (which might
# need to be edited by a user at a certain point in time) from the backend, which tells the
# script to read and print it. At this stage of my Python knowledge, I can say that this is 
# my most elegant software solution so far.

def zenOfPython():
    poem = open('Poem.txt', 'r')
    print(poem.read())
    
zenOfPython()