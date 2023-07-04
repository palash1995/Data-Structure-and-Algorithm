#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:50:43 2023

@author: palashchaudhari
"""

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        value = self.list.reverse()
        value = [str(x) for x in self.list]
        return '\n'.join(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self, value):
        if self.isFull():
            return "Stack is full.. Unable to load data!"
        else:
            self.list.append(value)
    
    def pop(self):
        if self.list == []:
            return "Stack is empty. No data to pop!"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.list == []:
            return "Stack is empty"
        else:
            return self.list[len(self.list)-1]
    
newStack = Stack(5)
newStack.push(1)
newStack.push(2)
newStack.push(3)
newStack.push(4)
newStack.push(5)
print(newStack)
print(newStack.pop())
print(newStack.pop())
print(newStack.pop())
print(newStack.peek())
print("Other Op")
print(newStack)
