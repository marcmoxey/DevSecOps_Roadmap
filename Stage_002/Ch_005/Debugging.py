# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:55:00 2026

@author: moxey
"""

# Raising Exceptions 
#raise Exception('This is the error message')


# Assertions 
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
#ages.sort()
print(ages)
#assert ages[0] <= ages[-1] # Assert that the first age is <= the last age

# Logging 
import logging 

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# Log files 
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')

import logging
logging.basicConfig(
    level=logging.DEBUG,           
    format=' %(asctime)s - %(levelname)s - %(message)s'
)
logging.debug('Some minor code and debugging details.')
logging.info('An event happened.')
logging.warning('Something could go wrong.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')


import logging
logging.basicConfig(
    level=logging.INFO, 
    format=' %(asctime)s - %(levelname)s - %(message)s'
)
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')

# Practice Question 
# spam = 5 

# assert spam > 10

# eggs = 'goodbye' 
# bacon = 'hello'

# assert eggs != bacon



