# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:08:16 2026

@author: moxey
"""

while True:
    print('Enter you age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password (letter and number only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')