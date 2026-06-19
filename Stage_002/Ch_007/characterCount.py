# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:45:19 2026

@author: moxey
"""

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)