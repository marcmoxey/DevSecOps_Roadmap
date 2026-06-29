# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:16:37 2026

@author: moxey
"""
# Color Text with Bext
import bext 
bext.fg('red')
print('This test is red')
bext.bg('blue')
print('Red text on a blue background is an ugly color scheme')
bext.fg('reset')
bext.bg('reset')
print('The test is normal again. Ah, much better')

import playsound3
from pathlib import Path 

# Sound and Text Notification
path = Path('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_012/hello.mp3')
playsound3.playsound(path)
