# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:08:06 2026

@author: moxey
"""

# Ending a ProgramEarly with sys.exit()

import sys

while True: 
    print('Type exit to exit')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('You type' + response + '.')