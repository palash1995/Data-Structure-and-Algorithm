#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:06:00 2023

@author: palashchaudhari
"""

    
number = 4
res = 1
for i in range(1, number+1):
    res = res*i
print(res)
count = 0    
while (res%10 == 0):
    count = count+1
    res = res//10
    
print(count)