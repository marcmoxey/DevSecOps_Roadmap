# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:43:22 2026

@author: moxey
"""

import time, sys

try:
    while True: # The main program loop
    # Draw lines with the increasing length
        for i in range(1,9):
            print('-' * (i * 1))
            time.sleep(0.1)
        
        # Draw lines with decreasing length:
        for i in range(7, 1, -1):
            print('-' * (i * 1))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
            