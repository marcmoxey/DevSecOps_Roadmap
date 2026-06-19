# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:59:25 2026

@author: moxey
"""

import random, sys, time

WIDTH = 70 # The number of columns 

try:
    # For each columns, when the counter is 0, no stream is shown
    # Otherwise, it acts as a counter for how many times a 1 or 0 should be displayed in the columns.
    columns = [0] * WIDTH
    while True:
        # Loop over each column 
        for i in range(WIDTH):
            if random.random() < 0.02:
                # Restart a stream counter on this column
                # The stream length is between 4 and 14 charcters long
                columns[i] = random.randint(4,14)
                # Print a charcter in this column:
            if columns[i] == 0:
                # Change this ' '' to '.' to see empty spaces:
                print('.',end='')
            else:
                # Print a 0 or 1:
                print(random.choice([0,1]), end='')
                columns[i] -= 1 # Decrement the counter for this column.
        print() # Print a newline at the end of the row columns
        time.sleep(0.1) # Each row pauses for tenth if a second
except KeyboardInterrupt:
    sys.exit()