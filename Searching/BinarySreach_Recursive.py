#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:29:41 2023

@author: palashchaudhari
"""
def BSearch(lst, x, low, high):
    if low > high:
        return
    mid = (low+high)//2
    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        low = mid+1
        return BSearch(lst, x, low, high)
    else:
        high = mid-1
        return BSearch(lst, x, low, high)
    return

lst = [10,20,30,40,50,60,70,80,90,100]
x = 80
BSearch(lst,x,0,len(lst)-1)
    