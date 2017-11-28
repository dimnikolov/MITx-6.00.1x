# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:05:16 2017

@author: Dimitar Nikolov
"""

currentYear = 2017

def registration():
    
    fName = input("Enter your first name... ")
    lName = input("Enter your last name... ")
    uYear = input("When were you born? ")
    uAge = 0
    uAge = (int(currentYear) - int(uYear))
    
    print("Your name is" + " " + fName + " " + lName + ". " + "And you are" + " " + str(uAge) + " " + "years old.")
    
registration()