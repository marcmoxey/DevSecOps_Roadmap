# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:49:18 2026

@author: moxey
"""

while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish)')
    password = input('>')
    if password == 'swordfish':
        break
print('Access granted')