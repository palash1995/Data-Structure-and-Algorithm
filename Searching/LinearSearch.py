#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:38:45 2023

@author: palashchaudhari
"""

def lSearch(lst,a):
    for i in lst:
        if i == a:
            print("The number available in list...")
            return 0
            
lst = [10,20,30,40,50,60,70,80]
a = 560
lSearch(lst,a)
