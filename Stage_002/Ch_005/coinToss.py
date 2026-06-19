# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:14:11 2026

@author: moxey
"""

import random 
guess = '' 
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss  = random.randint(0,1) # 0 is tails, 1 is heads
if toss == 0: 
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
if toss == guess:
    print('You got it')
else: 
    print('Nope! Guess again')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope, You are really bad at this game')