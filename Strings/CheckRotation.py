#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 01:51:46 2023

@author: palashchaudhari
"""

def checkRotation(s1,s2):
    if len(s1) != len(s2):
        return False

    temp=""
    temp = s1+s1
    return temp.find(s2)!=-1


s1 = "ABCD"
s2 = "CDAB"

a = checkRotation(s1,s2)
print(a)
