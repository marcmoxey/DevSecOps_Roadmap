# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:56:26 2026

@author: moxey
"""

import time 
# print(time.time())
print(time.ctime())
this_moment = time.time()
print(time.ctime(this_moment))

# Pasuing Programs 
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)
# time.sleep(5)


# The datetime Module 
import datetime, time

print(datetime.datetime.now())
dt = datetime.datetime(2026, 10, 21, 16, 29,0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

dt = datetime.datetime.fromtimestamp(10000000)
print(dt)
dt = datetime.datetime.fromtimestamp(time.time())
print(dt)

halloween_2026 = datetime.datetime(2026, 10,31,0, 0,0)
new_years_2027 = datetime.datetime(2027, 1,1, 0,0,0)
oct_31_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)
print(halloween_2026 == oct_31_2026)
print(halloween_2026 > new_years_2027)
print(new_years_2027 > halloween_2026)
print(new_years_2027 != oct_31_2026)

# Representing Durtion 
