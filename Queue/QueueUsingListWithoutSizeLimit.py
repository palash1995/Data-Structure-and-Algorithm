#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:25:23 2023

@author: palashchaudhari
"""
class Queue:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        value = [str(x) for x in self.list]
        return ' '.join(value)
    
    def enqueue(self, value):
        self.list.append(value)
        return "Data is enqueued..."
    
    def dequeue(self):
         self.list.remove(self.list[0])
         
    def peek(self):
        value = self.list[0]
        return value
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def delete(self):
        self.list = None
        
newQueue = Queue()
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
newQueue.enqueue(4)
newQueue.enqueue(5)
# print(newQueue)
print("Enqueue is completed..")
newQueue.dequeue()
newQueue.dequeue()
print("Dequeuq is completed..")
print(newQueue)
print(newQueue.peek())

