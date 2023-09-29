#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:54:48 2023

@author: palashchaudhari
"""

def bubbleSort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
    
lst = [20,10,40,30]
print(bubbleSort(lst))
