#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:44:14 2023

@author: palashchaudhari
"""

def fun(n):
    if n == 0:
        return
    fun(n//2)
    print(n%2)
    
fun(13)