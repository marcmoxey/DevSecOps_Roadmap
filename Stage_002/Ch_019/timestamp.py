# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:35:58 2026

@author: moxey
"""

# Measure how long it takes to multiply 100,100 numbers.
import time 
def caluclate_product():
    # Calculate the product of the first 100,000 numbers.
    product = 1 
    for i in range(1, 100001):
        product = product * i
    return product 

start_time = time.time()
result = caluclate_product()
end_time = time.time()
print(f"It took {end_time - start_time} seconds to calculate")