# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:22:05 2026

@author: moxey
"""

def comma(list_value):
    results = ''
    
    if len(list_value) == 0:
        return ''
    
    for i in range(len(list_value)):
        if i == len(list_value) -1:
            results += 'and ' + list_value[i]
        else:
            results += list_value[i] + ', '
    
    return results
    
spam = ['apples', 'bananas', 'tofu', 'cats']

print(comma(spam))
print(comma([]))