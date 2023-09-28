#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:45:43 2023

@author: palashchaudhari
"""
def fact(number):
    res = 1
    for i in range(1, number+1):
        res = res*i
    return res

if __name__ == '__main__':
    number = 6

    print(fact(number))
