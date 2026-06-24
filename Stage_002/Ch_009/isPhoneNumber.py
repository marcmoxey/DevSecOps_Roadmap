# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 07:38:33 2026

@author: moxey
"""

# Finding Text patterns Without Regular Expressions 

def is_phone_number(text):
    if len(text) != 12: # Phone numbers have exactly 12 characters
        return False
    for i in range(0,3): # The first three characters must be numbers 
        if not text[1].isdecimal():
            return False
    if text[3] != '-': # The foruth character must be a dash
        return False 
    for i in range(4,7): # The next three charcter must be numbers 
        if not text[i].isdecimal():
            return False
    if text[7] != '-': # The eigth charcater must be a dash
        return False
    for i in range (8,12): # The next four charcters must be numbers
        if not text[i].isdecimal():
            return False 
    return True

# print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
# print(is_phone_number('415-555-4242'))
# print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
# print(is_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found ' + segment)
print('Done')