#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 17:37:47 2023

@author: palashchaudhari
"""

def factorial(num):
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(4))