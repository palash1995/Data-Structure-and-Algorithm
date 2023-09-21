#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 23:31:01 2023

@author: palashchaudhari
"""

print(ord("a"))
print(ord("A"))
print(chr(97))
print(chr(65))


str = "San Francisco"
print(str)
print(str[0])
print(str[-1])


#String is immutable
# s = "Geek"
# s[0]="e"
# print(s)

#Triple quote 

s = """Hello,
       How are you doing today!
       Thanks for the head-up"""
print(s)

#printing new line
print("Hi John, \nHow are you today!")

#Escape sequence
print("How are \ you..")
#print("How are you \") - gives error
print("How are you \\")

#Raw String
print("c:\project\name.py") #\n treat as new line..
s = r"c:\project\name.py"
print(s)
