# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:55:38 2026

@author: moxey
"""

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
    
def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('d() starts')
    print('d() returns')
    

a()