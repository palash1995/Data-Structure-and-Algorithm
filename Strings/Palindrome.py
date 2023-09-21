#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 02:04:11 2023

@author: palashchaudhari
"""

#MEthod 1
def checkPalindrome(s1):
    temp =""
    temp = s1[::-1]
    if s1 == temp:
        return True
    else:
        return False


s1 = "AABAA"
a = checkPalindrome(s1)
print(a)


#Method 2

def checkPalindrome(s1):
    low = 0
    high = len(s1)-1
    
    while low < high:
        if s1[low] != s1[high]:
            print("Not a Palindrome..")
            break
        else:
            print("It is Palindrome...")
        
        low = low + 1
        high = high - 1
            
    
s1 = "ABCDDCBA"
a = checkPalindrome(s1)
