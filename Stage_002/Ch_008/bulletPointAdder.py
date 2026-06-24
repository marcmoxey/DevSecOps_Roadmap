# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:09:37 2026

@author: moxey
"""

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars 

lines = text.split('\n')
for i in range(len(lines)): # Loop through all indexes in "lines" listt
    lines[i] = '* ' + lines[i] # Add a star to each string in the lines list
text = '\n'.join(lines)
pyperclip.copy(text)
