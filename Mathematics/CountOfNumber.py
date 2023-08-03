#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:13:56 2023

@author: palashchaudhari
"""

num = input("Input Number:- ")

listOfNumber = [int(i) for i in num]
count = 0
for i in listOfNumber:
    count += 1

print(count)