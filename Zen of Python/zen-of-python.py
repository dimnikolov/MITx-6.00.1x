# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:34:04 2017

@author: Dimitar Nikolov
"""

def zenOfPython():
    
    # Store poem in variables
    poemTitle = 'The Zen of Python, by Tim Peters'
    line1 = 'Beautiful is better than ugly.'
    line2 = 'Simple is better than complex.'
    line3 = 'Complex is better than complicated.'
    line4 = 'Flat is better than nested.'
    line5 = 'Sparse is better than dense.'
    line6 = 'Readability counts.'
    line7 = "Special cases aren't special enough to break the rules."
    line8 = "Although practicality beats purity."
    line9 = "Errors should never pass silently."
    line10 = "Unless explicitly silenced."
    line11 = "In the face of ambiguity, refuse the temptation to guess."
    line12 = "There should be one-- and preferably only one --obvious way to do it."
    line13 = "Although that way may not be obvious at first unless you're Dutch."
    line14 = "Now is better than never."
    line15 = "Although never is often better than *right* now."
    line16 = "If the implementation is hard to explain, it's a bad idea."
    line17 = "If the implementation is easy to explain, it may be a good idea."
    line18 = "Namespaces are one honking great idea -- let's do more of those!"
    
    # There's probably a better, dynamic way to print variables from 1 to 18. I guess I will refactor this code later, when I know how to do so.
    
    poemContent = f"""
    {line1}
    {line2}
    {line3}
    {line4}
    {line5}
    {line6}
    {line7}
    {line8}
    {line9}
    {line10}
    {line11}
    {line12}
    {line13}
    {line14}
    {line15}
    {line16}
    {line17}
    {line18}"""
    
    # Print variables that contain poem
    print(poemTitle)
    print("================================")
    print(poemContent)
    
zenOfPython()