# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:19:14 2026

@author: moxey
"""

def spam():
    global eggs
    eggs = 'spam' # This is the global variable 
    
def bacon():
    eggs = 'bacon' # This is a local variable 

def ham():
    print(eggs) # This is the global variable 
    
eggs = 'global' # This is the global variable 
spam()
print(eggs)