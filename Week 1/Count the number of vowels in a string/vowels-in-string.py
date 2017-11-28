# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:55:40 2017

@author: dimitar.stoyanov
"""

string = input('Enter any word or sentence: ')

count = 0
vowels = set('aeiou')

for letter in string:
    if letter in vowels:
        count += 1
        
print("The number of vowels:", count)