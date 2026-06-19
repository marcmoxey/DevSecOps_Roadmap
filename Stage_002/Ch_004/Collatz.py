# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:53:17 2026

@author: moxey
"""

def collatz(number):
    if number % 2 == 0:
      print(number // 2)
      return number // 2
    elif number % 2 == 1:
       print(3 * number + 1, sep=' ')
       return(3 * number + 1)

number = int(input('Please enter a number: '))
while number != 1:
    number = collatz(number)
