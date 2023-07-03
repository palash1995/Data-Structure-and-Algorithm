#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 23:19:44 2023

@author: palashchaudhari
"""

class Node:
    def __init__(self, value):
        self. value = value
        self.next = None
        self.prev = None
        
class DoubleCLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode:
            result += str(tempNode.value)
            if tempNode.next is self.head:
                break
            if tempNode.next is not self.head:
                result += " -> "
            tempNode = tempNode.next
        return result
    
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            newNode.next = self.head
        self.length += 1
            
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
        self.length += 1
        
    def insert(self, value, index):
        newNode = Node(value)
        if self.head is None:
            self.head = None
            self.tail = None
            newNode.next = newNode
        elif index == 0:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
        elif index == self.length:
            print("I am here")
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = self.head
        else:
            tempNode = self.head
            for _ in range(index-1):
                tempNode = tempNode.next
            newNode.next = tempNode.next
            newNode.prev = tempNode
            tempNode.next = newNode
            tempNode.next.prev = newNode
        self.length += 1
        
    def popFirst(self):
        tempNode = self.head
        self.head = tempNode.next
        self.tail.next = self.head
        tempNode.next = None
        tempNode.prev = None
        return tempNode.value
    
    def pop(self):
        tempNode = self.tail
        self.tail = self.tail.prev
        self.tail.next = self.head
        tempNode.next = None
        tempNode.prev = None
        return tempNode.value
    
    def transversal(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            if tempNode.next is self.head:
                break
            tempNode = tempNode.next
            
    def search(self, target):
        tempNode = self.head
        index = 0
        while tempNode:
            if tempNode.value == target:
                return index
            if tempNode.next is self.head:
                break
            index += 1
            tempNode = tempNode.next
            
    def getValue(self, index):
        tempNode = self.head
        for _ in range(index):
            tempNode = tempNode.next
        return tempNode
    
    def setValue(self, value, index):
        tempNode = self.getValue(index)
        if tempNode:
            tempNode.value = value
            
    def remove(self, index):
        if index == 0:
            tempNode = self.head
            self.head = tempNode.next
            self.tail.next = self.head
            tempNode.next = None
            tempNode.prev = None
        elif index == self.length-1:
            tempNode = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            tempNode.next = None
            tempNode.prev = None
        else:
            tempNode = self.head
            for _ in range(index):
                tempNode = tempNode.next
            tempNode.prev.next = tempNode.next
            tempNode.next.prev = tempNode.prev
            tempNode.next = None
            tempNode.prev = None
        self.length -= 1            
            
            
            
newDoubleCLL = DoubleCLL()
newDoubleCLL.append(0)
newDoubleCLL.append(1)
newDoubleCLL.append(2)
newDoubleCLL.append(3)
newDoubleCLL.append(4)
newDoubleCLL.append(5)
print(newDoubleCLL)
# newDoubleCLL.prepend(0)
# newDoubleCLL.prepend(-1)
# newDoubleCLL.insert(88,6)
# newDoubleCLL.popFirst()
# newDoubleCLL.popFirst()
# newDoubleCLL.pop()
# newDoubleCLL.pop()
# newDoubleCLL.transversal()
# print(newDoubleCLL.search(4))
# print(newDoubleCLL.getValue(5))
# print(newDoubleCLL.setValue(88,4))
newDoubleCLL.remove(6)
print(newDoubleCLL)
