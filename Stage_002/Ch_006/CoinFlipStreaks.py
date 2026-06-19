# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:31:19 2026

@author: moxey
"""

import random

number_of_streaks = 0

for experiment_number in range(10000):
    coins = []

    # create 100 random H/T values
    for i in range(100):
        if random.randint(0, 1) == 0:
            coins.append('H')
        else:
            coins.append('T')

    # check for streaks of 6
    for i in range(95):
        if coins[i:i+6] == ['H','H','H','H','H','H'] or coins[i:i+6] == ['T','T','T','T','T','T']:
            number_of_streaks += 1
            break

print('Chance of streak: %s%%' % (number_of_streaks / 100))