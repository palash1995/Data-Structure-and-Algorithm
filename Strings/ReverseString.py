#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 01:31:03 2023

@author: palashchaudhari
"""

string = "GEEKS"

#method 1
rev =""
for i in string:
    rev = i + rev

print((rev))

#method 2
print(string[::-1])
