# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:19:47 2026

@author: moxey
"""

import pyperclip, os, sys
if (sys.argv) > 1:
    os.chdir(sys.argv[1])
pyperclip.copy(os.getcwd())