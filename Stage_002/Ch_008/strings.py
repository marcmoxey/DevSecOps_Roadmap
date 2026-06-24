# Working with Strings 

# String Literals 

#Double quotes 

spam = "That is Alice's cat."


# Escape charcters 
spam = 'Say hi tp bob\'s mother.'
print("Hello there!\nHow are you?\nI\'m doing fine")


# Raw Strings
print(r'The file is in C:\Users\Alice\Desktop') # 'r' - raw string 
print('Hello....\n\n....world!') # without a raw string
print(r'Hello...\n\n...world!')  # With a raw string


# Multiline Comments 
"""This is a test Python program.
Writting by al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2 
"""

def say_hello():
    """This function prints hello"""
    print('Hello')
    
    
    
# Indexes and Slices 
greeting = 'Hello, world!'
print(greeting[0])
print(greeting[4])
print(greeting[-1])
print(greeting[0:5])
print(greeting[:5])
print(greeting[7:-1])
print(greeting[7:])


greeting = 'Hello, world!'
greeting_slice = greeting[0:5]
print(greeting_slice)
print(greeting)


# The in and not in operators 
print('Hello' in 'Hello, world!')
print('Hello' in 'Hello')
print('HELLO' in 'Hello, World!')
print('' in 'spam')
print('cats' not in 'cats and dogs')


# F-Strings 
name = 'Ai'
age = 4000
print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old')
print('In tens years I will be ' + str(age + 10))

print(f'My name is {name}. I am {age} years old')
print(f'In 10 years I will be {age+10}')

name = 'Zophie'
print(f'{name}')
print(f'{{name}}') # Double curly brackets are literal curly brackets.


# F-String Alternatives: %s and format()
name = 'Al'
age = 4000

print('My name is %s. I am %s years old' % (name,age))
print('In ten years I will be %s' % (age+10))

name = 'Al'
age = 4000

print('My name is {}. I am {} years old.'.format(name,age))
print('My name is {0}. I am {0} years old.'.format(name,age)) # You can put the index integer (starting at 0) inside the curly brackets to note which of the arguments to format()


# Useful string Methods
spam = 'Hello, world!'
spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the resst of your day is good.')

spam = 'Hellom world!'
print(spam.islower())
print(spam.isupper())
print('HELLO'.isupper())
print('abc12345'.isupper())
print('12345'.islower())
print('12345'.isupper())

print('Hello'.upper())
print('hello'.upper().lower())
print('hello'.upper().lower().upper())
print('Hello'.lower())
print('Hello'.lower().islower())


# Checking String Characteristics 
print('hello'.isalpha()) # Returns True if the string consists only of letters and isn’t blank
print('hello123'.isalpha())
print('hello'.isalnum()) # Returns True if the string consists only of letters and numbers (alphanumerics) and isn’t blank
print('hello'.isalnum())
print('123'.isdecimal()) # Returns True if the string consists only of numeric characters and isn’t blank
print('     '.isspace()) # Returns True if the string consists only of spaces, tabs, and newlines and isn’t blank
print('THis is a Title Case'.istitle()) # Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters


# Checking and the Start or End of a String
print('Hello, world1'.startswith('Hello'))
print('Hello, world!'.endswith('world!'))
print('abcd'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello, world!'.startswith('Hello, world!'))
print('Hello, world!'.endswith('Hello, world!'))

# Joining and Spliting Strings 
print(', '.join(['cats','rats','bats']))
print(' '.join(['My','name','is','Simon']))
print('ABC'.join(['My','name','is','Simon']))
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))\
    
spam = '''Dear Alice,
There is a milk bootle in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))


# Justifying and Centering Text 
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello, world!'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20,'-'))
print('Hello'.center(20))
print('Hello'.center(20,'='))


# Removing White space
spam = '       Hello, World             '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))


# Numeric Code Points of Characters 
print(ord('A'))
print(ord('4'))
print(ord('!'))
print(chr(65))
print(ord('B'))
print(ord('A') < ord('B'))
print(chr(ord('A')))
print(chr(ord('A')+1))



# Copying and Pasting Strings 
import pyperclip
# pyperclip.copy('Hello, world!')
# print(pyperclip.paste())
print(pyperclip.paste())