# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:41:54 2026

@author: moxey
"""
# The Dictionary Data Type
my_cat = {'size':'fat', 'color': 'gray', 'age':17}
print(my_cat['size'])
print('My cat has ' + my_cat['color'] + ' fur.')
spam = {12345 : 'Luggage Combination', 42: 'The Answer'}
print(spam[12345])
print(spam[42])
# print(spam[0]) # error - KeyError: 0


# Comparing Dictionaires and Lists -  items in dictionaries are unordered
spam = ['cat', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # The order of List items matter

eggs = {'name': 'Zophie', 'species': 'cat', 'age' :'8'}
ham = {'species':'cat', 'age':'8', 'name': 'Zophie'}
print(eggs == ham) # The order of dictionary key-value pairs doesn't matter.

spam = {'name':'Zophie', 'age':7}
# print(spam['color']) # KeyError: 'color'



# Returning Keys and Values 
spam = {'color':'red', 'age':42}
for v in spam.values():
    print(v)
    
for k in spam.keys():
    print(k)
    
print('color' in spam.keys())
print('age' not in spam.keys())
print('red' in spam.values())
for i in spam.items():
    print(i)
    
    
print('color' in spam)
print('color' in spam.keys())

spam = {'color':'red', 'age':42}
print(spam.keys())
print(list(spam.keys()))

spam = {'color':'red', 'age':42}
for k, v in spam.items():
    print('Key: ' + str(k) + ' Value: ' + str(v))
    
    
# Checking Whether Key Exists 
picnic_items = {'apples':5, 'cups':2}
print('I am bringing ' + str(picnic_items.get('cups',0))+ ' cups.')
print('I am bringing ' + str(picnic_items.get('eggs',0))+ ' eggs.')


# Setting Default Values 
spam = {'name': 'Pooka', 'age':5}
if 'color' not in spam:
    spam['color'] = 'black'

print(spam)

spam = {'name': 'Pooka', 'age':5}
spam.setdefault('color','black') # sets 'color' key to 'black'
print(spam)
spam.setdefault('color', 'white')  # Does nothing
print(spam)
 
