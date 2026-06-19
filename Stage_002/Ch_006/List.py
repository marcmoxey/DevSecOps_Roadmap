# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 06:28:18 2026

@author: moxey
"""

# List Data Type
print([1,2,3]) # List of three integers
print(['cat','bat','rat','elephant']) # A list of four string 
print(['hello', 3.1415, True, None, 42]) # A list of serval values 
spam = ['cat','bat','rat','elephant']
print(spam)


# Indexes -  first index dictates which list value to use, and the second indicates the value within the list
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print( ['cat','bat','rat','elephant'][3])
print('Hello ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')
#print(spam[1000]) # Error - IndexError: list index out of range
spam = [['cat','bat'], [10,20,30,40,50]]
print(spam[0]) # ['cat', 'bat']
print(spam[0][1]) # bat
print(spam[1][4])


# Negative Indexes - The integer value -1 refers to the last index in a list
spam = ['cat','bat','rat','elephant']
print([spam[-1]]) # last index
print(spam[-3]) # Third to last index
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')


# Slices - can get several values from a list, in the form of a new lis
print(spam[0:4]) 
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(spam[:])


# The len function - return the number of values in a list value passed to it
print(len(spam))


# Value Updates 
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)

# Concation and Replication 
print([1,2,3] + ['A','B','C'])
print(['X','Y','Z'] * 3)
spam = [1,2,3]
spam = spam + ['A','B','C']
print(spam)


# del Statements - delete values at an index in a list
spam = ['cat','bat','rat','elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)


# for loops and Lists 
supplies = ['pens','staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supples is: ' + supplies[i])


# The in and not in Operators 
print('hodwy' in ['hello','hi','hodwy', 'heyas'])
spam = ['hello','hi','hodwy', 'heyas']
print('cat' in spam)
print('hodwy' not in spam)
print('cat' not in spam)


# The Multiple Assigment Trick
cat = ['fat', 'gray', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

size, color,dispostion = cat
print(cat)


# List item Enumeration - enumerate() will return two values: the index of the item in the list, and the item in the list itself.
supplies = ['pens','staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
    


# Random Selection and Ordering - will return a randomly selected item from the list
import random
pets = ['Dog', 'Cat', 'Mouse']
print(random.choice(pets))

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)


# Augmented Assignments Operators 
spam = 'Hello'
spam += ' wolrd!'
print(spam)
bacon = ['Zophie']
bacon *= 3 
print(bacon)


# Methods 
spam = ['hello', 'hi', 'hodwy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))


# When the list contains duplicates of the value, the method returns the index of its first appearance:
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

# Append
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)


# eggs = 'hello'
# eggs.append('world') # error - can only append to a list

spam = ['cat','bat','rat','elephant'] 
spam.remove('bat')
print(spam)


# Remove
# spam.remove('chicken') # error - can only remove item that in a lsit
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') # remove only the first instance of it
print(spam)

# Sorting Values 
spam = [2,5,3.14,1,-7]
spam.sort()
print(spam)

spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort()
print(spam)

spam = [1,2,3,4,'Alice', 'Bob']
#spam.sort() # error - TypeError: '<' not supported between instances of 'str' and 'int'
#print(spam) 

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()  # uppercase gonna come first casue of ASCIIbetical order rather than actual alphabetical order for sorting strings
print(spam)
spam = ['a','z','A','Z']
spam.sort(key=str.lower)
print(spam)

# Reversing Values
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)

# Short-Circuiting Boolean Operators
spam = []
if len(spam) > 0 and spam[0] == 'cat':
    print('A cat is the fist item')
else: 
    print('The first item is not a cat')
    
    
# Sequence Data Types 
name = 'Zophia'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' not in name)
for i in name:
    print('***'+ i + '***')
    
    
# Mutable and Immutable Data Types - A list value is a mutable data type: you can add, remove, or change its values. However, a string is immutable: it cannot be changed.

name = 'Zophie a cat'
# name[7] = 'the' # error - TypeError: 'str' object does not support item assignment
# print(name)
new_name = name[0:7] + 'the' + name[8:12]
print(name)
print(new_name)

eggs = ['A', 'B', 'C']
eggs = ['x', 'y' 'z']
print(eggs) # eggs isn’t being changed here rather, a new and entirely different list value 


# eggs variable ends up with the same list value it started with. It’s just that this list has been changed (mutated) rather than overwritten
eggs = ['A', 'B', 'C'] 
del eggs[2]
del eggs[1]
del eggs[0]

eggs.append('x')
eggs.append('y')
eggs.append('z')
print(eggs)

# The Tuple Data Type - write tuples using parentheses - immutable: you can’t modify, append, or remove their values
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

eggs = ('hello', 42, 0.5)
#eggs[1] = 99 # TypeError: 'tuple' object does not support item assignment
#print(eggs)

print(type(('hello',)))
print(type('hello'))


# List and Tuples Type Conversion
print(tuple(['cat','dog',5]))
print(list(('cat','dog',5)))
print(list('hello'))


# Refernaces 
spam = 42
eggs = spam 
spam = 99
print(spam)
print(eggs)


spam = [0,1,2,3]
eggs = spam # The refernce, not the list, is being copied 
eggs[1] = 'Hello' # This change the list value
print(spam)


# Arguments 
def eggs(some_parameter):
    some_parameter.append('hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)


# The copy() and deepcopy Functions - .copy(), can make a duplicate copy of a mutable value like a list or dictionary, creates a completely independent copy of an object, recursively duplicating all nested elements so that modifications to the copy do not affect the origina

import copy 
spam = ['A','B','C']
cheese = copy.copy(spam) # Create a duplicate copy of the list 
cheese[1] = 42 # changes cheese
print(spam)
print(cheese)
 
spam = ['a', 'b', 'c', 'd']
print(spam[int(int('3' * 2) // 11)])