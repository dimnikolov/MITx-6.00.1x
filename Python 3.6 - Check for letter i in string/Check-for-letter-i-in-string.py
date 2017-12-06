# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:07:55 2017

@author: Dimitar Nikolov
"""

s = input("Enter a string... ")

for index in range(len(s)):
    if s[index] == 'i':
        print("There is an 'i'")
    else:
        print("There is no 'i' in your string.")
        break # Break the loop to not print the message more than once.