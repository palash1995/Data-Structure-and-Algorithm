#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 02:34:18 2023

@author: palashchaudhari
"""
# Check if a String is Subsequence of Other

def issubseq(s1,s2) :
    i, j = 0, 0
    while(i < len(s1) and j < len(s2)) :
        if s1[i] == s2[j] :
            j = j + 1 
        i += 1 
    if j == len(s2) :
        return True
    else :
        return False
        
s1 = "ABDESDZ"
s2 = "ABZ"

print(issubseq(s1,s2))
