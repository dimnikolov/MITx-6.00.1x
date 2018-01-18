# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:58:37 2017

@author: Dimitar Nikolov
"""

# Add x and y
def add(x, y):
    return x + y

# Subtract x and y
def subtract(x, y):
    return x - y

# Multiply x and y
def multiply(x, y):
    return x * y

# Divide x and y
def divide(x, y):
    return x / y

print("""Select an operation:
    
    1. Add:         To add x and y (x+y), enter '1'
    2. Subtract:    To subtract x and y (x-y), enter '2'
    3. Multiply:    To multiply x and y (x*y), enter '3'
    4. Divide:      To divide x and y (x/y), enter '4'
    ====================================================
    5. Quit:        To quit this program, enter '6'""")
    
user_choice = input("Enter your choice: ")
 
if user_choice == '1':
    print("For the formula (x + y) = z")
    x = float(input("Enter x = "))
    y = float(input("Enter y = "))
    print("\nz =", add(x,y))
    
elif user_choice == '2':
    print("For the formula (x - y) = z")
    x = float(input("x = "))
    y = float(input("y = "))
    print("\nz =", subtract(x,y))  
    
elif user_choice == '3':
    print("For the formula (x * y) = z")
    x = float(input("x = "))
    y = float(input("y = "))
    print("\nz =", multiply(x,y))  

elif user_choice == '4':
    print("For the formula (x / y) = z")
    x = float(input("x = "))
    y = float(input("y = "))
    print("\nz =", divide(x,y))  
    
elif user_choice == '5':
    print("Program has terminated")
    
else:
    print("Invalid input. Please try again.")
    
