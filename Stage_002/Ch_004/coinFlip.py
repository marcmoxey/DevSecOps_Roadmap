# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:51:54 2026

@author: moxey
"""

import random 

for i in range(100): # Perform 100 coin flips
    if random.randint(0,1) == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
print() # Print one newline at the end