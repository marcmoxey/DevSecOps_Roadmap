# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:21:08 2026

@author: moxey
"""

#  Englist to pig latin
print('Enter the English message to translate into pig latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = [] # A list of the words in pig latin
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue
    
    # Separate the non-letters at the end of this word
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]
        
    # Remeber if the word was in uppercase or title case:
    was_upper = word.isupper()
    was_lower = word.islower()
    
    word = word.lower() # make the word lowercase for translation
    
    # Separate the consontants at the start of the word:
    prefix_consonats = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonats += word[0]
        word = word[1:]
        
    # Add the pig latin ending to the word
    if prefix_consonats != '':
        word += prefix_consonats + 'ay'
    else:
        word += 'yay'
        
    # Set the word back to uppercase or title case
    if was_upper:
        word = word.upper()
    else:
        word = word.title()
        
    # Add the non-letters back to the start or end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join all the words back together into a single string
print(' '.join(pig_latin))
        