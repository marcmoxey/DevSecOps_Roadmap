# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 08:26:05 2026

@author: moxey
"""

my_pets = ['Zophie','Pooka','Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pets:
    print('I do not have any pet name ' + name)
else: 
    print(name + ' is my pet')
