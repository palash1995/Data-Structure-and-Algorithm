#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:58:08 2023

@author: palashchaudhari
"""

def sumOfDigit(n):
    if n == 0:
        return
    return (n//10) + (n%10)

sumOfDigit(32)