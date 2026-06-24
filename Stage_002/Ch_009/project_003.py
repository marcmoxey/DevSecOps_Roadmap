# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 07:29:20 2026

@author: moxey
"""
import pyperclip, re

# Step 1: Create a Regex for Phone Numbers
phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)


# Step 2: Create a Regex for Email Addresses
# TODO: Create Email regex
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #  Username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # Domain name
    (\.[a-zA-Z]{2,4}) # Dot something
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text 
# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)
for groups in email_re.findall(text):
    matches.append(groups[0])



# TODO: Copy result to the clipboard 
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else: 
    print('No phone number or email address found')
