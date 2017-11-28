# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:34:04 2017

@author: Dimitar Nikolov
"""

# This is Iteration 2, or the first refactoring of my Zen of Python script.
# Instead of storing each poem line in a separate variable, I have created a list.
# I then use the syntax of Python for accessing list elements by index positions.

def zenOfPython():
    
    # Store poem in variables
    
    ## Store poem title
    poemTitle = 'The Zen of Python, by Tim Peters'
    ## Store poem content
    poemLines = ['Beautiful is better than ugly.', 'Simple is better than complex.', 'Complex is better than complicated.',
                   'Flat is better than nested.', 'Sparse is better than dense.', 'Readability counts.', "Special cases aren't special enough to break the rules.",
                   'Although practicality beats purity.', 'Errors should never pass silently.', 'Unless explicitly silenced.',
                   'In the face of ambiguity, refuse the temptation to guess.', 'There should be one -- and preferably only one -- obvious way to do it.',
                   "Although that way may not be obvious at first unless you're Dutch.", 'Now is better than never.',
                   'Although never is often better than *right* now.', "If the implementation is hard to explain, it's a bad idea.",
                   'If the implementation is easy to explain, it may be a good idea.', "Namespaces are one honking great idea -- let's do more of those!"]
    
    poem = poemLines[0:18]
    
    # Print variables that contain poem
    print(poemTitle)
    print("================================")
    print(*poem)
    
zenOfPython()