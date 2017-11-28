# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:05:16 2017

@author: Dimitar Nikolov
"""

s = 'alicebobobjohnsmithbart'

total = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        total += 1
print ('The string is:' + ' ' + str(s))
print ('Number of times that bob occurs in the string' + ' "' + str(s) + '" ' + 'is ' + str(total))