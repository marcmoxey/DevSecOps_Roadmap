# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:04:39 2026

@author: moxey
"""

import pyperclip, time 

print('Recording clipboard... (Ctrl-C to stop)')
previous_content = ''
try: 
    while True:
        content = pyperclip.paste() # Get clipboard contetns 
        
        if content != previous_content:
            # If it's differnt from the previous, print it:
            print(content)
            previous_content = content
        
        time.sleep(0.01) # Pasue to avoid hoggin the cpu.
except KeyboardInterrupt:
    pass