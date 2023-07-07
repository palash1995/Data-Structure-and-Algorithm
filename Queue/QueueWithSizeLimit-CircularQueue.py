#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 12:41:03 2023

@author: palashchaudhari
"""

class Queue:
    def __init__(self, maxSize):
        self.item = maxSize*[None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        value = [str(x) for x in self.item]
        return ' '.join(value)
    
    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full..."
        else:
            if self.top+1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
        self.item[self.top] = value
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty.."
        else:
            firstElement = self.item[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start+1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.item[start] = None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty.."
        else:
            return self.item[self.start]
    
    def delete(self):
        self.list = self.maxSize*[None]
        self.top = -1
        self.start = -1

newQueue = Queue(3)
# print(newQueue.isFull())
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
print(newQueue)
print(newQueue.dequeue())
print(newQueue.dequeue())
print(newQueue.peek())
print(newQueue)