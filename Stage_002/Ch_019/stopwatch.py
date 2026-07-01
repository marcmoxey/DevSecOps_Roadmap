# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:40:41 2026

@author: moxey
"""

# Step 1: Set up the program to track times 

# A simple stopwatch program
import time 

# Display the program's instructions.
print('Press Enter to begin and mark laps. Ctrl-C quits')
input() # Press Enter to begin
print('Started')
start_time = time.time() # Get the first lap's start time.
last_time = start_time
lap_number = 1 


# TODO: Start tracking the lap time 
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap #{lap_number}: {total_time}({lap_time})", end='')
        lap_number += 1
        last_time = time.time() # Reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep it's error message from display
    print('\nDone')