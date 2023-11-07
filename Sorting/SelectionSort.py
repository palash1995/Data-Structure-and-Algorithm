#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:59:38 2023

@author: palashchaudhari
"""

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1,len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[min_index], customList[i] = customList[i], customList[min_index]
    print(customList)
        
lst = [3,6,1,8,7]
selectionSort(lst)