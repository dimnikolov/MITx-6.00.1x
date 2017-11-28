# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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