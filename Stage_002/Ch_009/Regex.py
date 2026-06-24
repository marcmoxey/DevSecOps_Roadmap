# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:07:46 2026

@author: moxey
"""

# Finding Text Patterns with Regular Expressions 
import re 
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242')
# match_obj.group()
print(match_obj.group())


# The Syntax of Regular Expression 


# Grouping with Parentheses 
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242')
print(mo.group(1)) # Returns the first group of the matched text
print(mo.group(2)) # Returns the second group of the matched text 
print(mo.group(0)) # Returns the full matched text
print(mo.group() ) # Also returns the full matched text)


area_code, main_number = mo.groups()
print(area_code)
print(main_number)


# Using Escape Charcters 
pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = pattern.search('My phone number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))


# Matching Characters from Alternate Groups 
pattern = re.compile(r'Cat(cerpiler|astrophe|ch|egory)')
match = pattern.search('Catch me if you can')
print(match.group())
print(match.group(1))


# Returning All Matches
pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # This regax has no group
result = pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # This regax has groups
result = pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

pattern = re.compile(r'\d{3}')
result = pattern.findall('1234')
print(result)

result = pattern.findall('12345')
print(result)

result = pattern.findall('123456')
print(result)


# Qualifer Syntax: What Characters to Match 
# Using Characters Classes and Negative Charcter classes 
vowel_pattern = re.compile(r'[aeiouAEIOU]')
result = vowel_pattern.findall('RoboCop eats BABY FOOD')
print(result)

# Outside brackets:
# ( and ) are special tools (they group things)

# Inside brackets:
# they are just normal characters

consonant_pattern = re.compile(r'[^aeiouAEIOU]') # '^' match all the characters that are not in the character class
result = consonant_pattern.findall('RoboCop eats BABY FOOD')
print(result)


# Using Shorthand Character Classes 
pattern = re.compile(r'\d+\s\w+')
result = pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(result)


# Matching Everything with the Dot Character 
at_re = re.compile(r'.at')
result = at_re.findall('The cat in the hat sat on the flat mat.')
print(result)


# Quantifer Syntax: How many Qualifers to Match 
# pattern = re.compile(r'42!?') # ? part of the regular expression means that the pattern ! is optional.
pattern = re.compile(r'42?!')
print(pattern.search('42!'))
print(pattern.search('42'))
print(pattern.search('4!'))
print(pattern.search('42') == None) # no match

pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 = pattern.search('My number is 415-555-4242')
print(match1.group())

match2 = pattern.search('My number is 555-4242')
print(match2.group())

# Matching Zero or more Qualifers - * means “match zero or more,”
pattern = re.compile('Eggs (and spam)+')
result = pattern.search('Eggs and spam')
print(result)

result = pattern.search('Eggs and spam and spam')
print(result)

result = pattern.search('Eggs and spam and spam and spam')
print(result)


# Matching a Specifc Number of Qualifers 
haRegex = re.compile(r'(Ha){3}')
match1 = haRegex.search('HaHaHa')
print(match1.group())

match = haRegex.search('Haha')
print(match == None)


# Greedy and Non-greedy Matching
greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHa')
print(match1.group())

lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group())

# The ? quantifier is the same as {0,1}.
# The * quantifier is the same as {0,}.
# The + quantifier is the same as {1,}.


# Matching Everything
name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
result = name_match.group(1)
print(result)
result = name_match.group(2)
print(result)

lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner.>')
result = match1.group()
print(result)

greedy_re = re.compile(r'<.*>')
match2 = greedy_re.search('<To serve man> for dinner.>')
result = match2.group()
print(result)

# Matching Newline Characters 
no_newline_re = re.compile('.*')
result = no_newline_re.search('Server the public trust.\nProtect the innocent.\nUphold the law.').group()
print(result)

newline_re = re.compile('.*', re.DOTALL)
result = newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(result)


# Matching at the Start and End of a string 
begins_with_hello = re.compile(r'^Hello')
result = begins_with_hello.search('Hello, world!')
print(result)
print(begins_with_hello.search('He said "Hello."') == None)

ends_with_number = re.compile('r\d$')
result = ends_with_number.search('Your number is 42')
print(result)
print(ends_with_number.search('Your number is forty two.') == None)


pattern = re.compile(r'\bcat.*?\b')
result = pattern.findall('The cat found a catapult catalog in the catacombs')
print(result)


pattern = re.compile(r'\Bcat\B')
result = pattern.findall('cartifcate') # Match
print(result)
result = pattern.findall('catastrophe') # No match 
print(result)


# A REVIEW OF REGEX SYMBOLS
# The ? matches zero or one instance of the preceding qualifier.
# The * matches zero or more instances of the preceding qualifier.
# The + matches one or more instances of the preceding qualifier.
# The {n} matches exactly n instances of the preceding qualifier.
# The {n,} matches n or more instances of the preceding qualifier.
# The {,m} matches 0 to m instances of the preceding qualifier.
# The {n,m} matches at least n and at most m instances of the preceding qualifier.
# {n,m}? or *? or +? performs a non-greedy match of the preceding qualifier.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# The \d, \w, and \s match a digit, word, or space character, respectively.
# The \D, \W, and \S match anything except a digit, word, or space character, respectively. [abc] matches any character between the square brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the square brackets.
# (Hello) groups 'Hello' together as a single qualifier.


# Case-Insensitive Matching 
pattern1 = re.compile('RoboCop')
pattern2 = re.compile('ROBOCOP')
pattern3 = re.compile('robOcop')
pattern4 = re.compile('RobocOp')

pattern = re.compile(r'robocop', re.I)
result = pattern.search('Robocop is part man, part machine, all cop.').group()
print(result)

result = pattern.search('ROBOCOP protects the incocent').group()
print(result)

result = pattern.search('Have you seen robocop?').group()
print(result)


# Substring Strings
agent_pattern = re.compile(r'Agent \w+')
result = agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob')
print(result)

agent_pattern = re.compile(r'Agent (\w)\w*')
result = agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob')
print(result)


# Managing Complex Regexes With Verbose Mode
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)


# Combining re.IGNORECASE, re.DOTALL and re.VERBOSE
some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


# Humre: A Module for Human-Readable Regexes 
from humre import *
phone_regex = exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
print(phone_regex)

pattern = re.compile(phone_regex)
result = pattern.search('My Number is 415-555-4242')
print(result)

import humre
print(humre.parse(r'\d{3}-\d{3}-\d{4}'))
