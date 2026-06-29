# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:38:08 2026

@author: moxey
"""

import os, random, time, sys 

TOP = chr(9600) # Character 9600 is '▀'
BOTTOM = chr(9604) # Character 9604 is '▄'
FULL = chr(9608) # Character is '█'

# Set the snowstorm density to the command line argument:
DENSITY = 4 # Default snow density is 4%
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

while True: 
    clear() # Clear the terminal window
    
    # Loop over each row and columns
    for y in range(20):
        for x in range(40):
            if random.randint(0,99) < DENSITY:
                # Print snow:
                print(random.choice([TOP,BOTTOM]), end='')
            else:
                # Print empty space:
                print('', end='')
        print() # Print a new line
        
    print(FULL * 40 + '\n' + FULL * 40)
    print('(Ctrl-C to stop.)')
    
    time.sleep(0.2) # pasue for a bit