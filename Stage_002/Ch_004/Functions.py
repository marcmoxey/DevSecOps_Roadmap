# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:47:44 2026

@author: moxey
"""

# The None values 

spam = print('Hello!')
print(spam) # None
print(None == spam)

# Name Parameters 
print('Hello', end='') # Python no longer prints a newline after 'Hello'. Instead, it prints a blank string
print('World')


print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')

# Locals and Global Scoops 

# def spam():
#     eggs = 'SPAMSPAM'
#     bacon()
#     print(eggs)
    
#spam()
#print(eggs) # error - NameError: name 'eggs' is not defined - eggs is a local scope 

# def bacon():
#     ham = 'hamham'
#     eggs = 'BACONBACON'

# spam()

# def spam():
#     print(eggs) # Prints 'GLOBALGLOBAL'
# eggs = 'GLOBALGLOBAL'
# spam()
# print(eggs)
    
# def spam():
#     eggs = 'spam local'
#     print(eggs) # Prints 'spam local'

# def bacon():
#     eggs = 'bacon local'
#     print(eggs) # prints 'bacon local'
#     spam()
#     print(eggs) # Prints 'bacon local'
    
# eggs = 'global'
# bacon()
# print(eggs) # Print global

# def spam():
#   global eggs
#   eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs)  # Prints 'spam'


# Exception Handling 
def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
            return 42 / divide_by
    except ZeroDivisionError:
        # If ZerodivisionError happened, the code in this block runs:
        print('Error: invalid argument')
        

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


