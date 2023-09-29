#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:38:53 2023

@author: palashchaudhari
"""

def selectionSort(lst):
    n = len(lst)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j             
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
    return lst
        
lst = [20,10,40,30]
print(selectionSort(lst))  