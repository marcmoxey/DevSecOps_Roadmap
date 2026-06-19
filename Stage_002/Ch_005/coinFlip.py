# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:05:29 2026

@author: moxey
"""

import random 
heads = 0 
for i in range(1,1001):
    if random.randint(0,1) == 1:
        heads += 1 
    if i == 500:
        print('Half way done!')
print('Heads came up ' + str(heads) + ' times.')