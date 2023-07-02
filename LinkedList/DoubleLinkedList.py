#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 00:25:58 2023

@author: palashchaudhari
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    # Review this code and try to figure out why it is not working
    # def __str(self)
    #     if self.head is None:
    #         return "LinkedList is empty!!"
    #     else:
    #         tempNode = self.head
    #         result =''
    #         while tempNode:
    #             result = result + str(tempNode.value)
    #             if tempNode.next is not None:
    #                 result += " -> "
    #             tempNode = tempNode.next
    #         return result            
            
        
    def __str__(self):
        tempNode = self.head
        result =''
        while tempNode:
            result = result + str(tempNode.value)
            if tempNode.next is not None:
                result += " -> "
            tempNode = tempNode.next
        return result
        
    def insertFirstNode(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        print(self.head)
        print(newNode.value)
        
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
            
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        
    
    def pop_first(self):
        tempNode = self.head
        self.head = tempNode.next
        tempNode.next = None
        self.length -= 1
        return tempNode.value  
    
    def pop(self):
        tempNode = self.tail
        self.tail = tempNode.prev
        tempNode.prev = None
        self.tail.next = None
        self.length -= 1
        return tempNode.value
    
    def insert(self, value, index):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        elif index == self.length-1:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        elif index < 0 or index >= self.length:
            return "Invalid Index"
        else:
            tempNode = self.head
            for _ in range(index-1):
                tempNode = tempNode.next
            newNode.next = tempNode.next
            newNode.prev = tempNode
            tempNode.next = newNode
            newNode.next.prev = newNode
        self.length += 1
        
    def transversal(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
            
    def search(self, target):
        tempNode = self.head
        index = 0
        while tempNode:
            if tempNode.value == target:
                return index
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
            return
        return False
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return "Invalid index"
        elif index == 0:
            tempNode = self.head
            self.head = tempNode.next
            self.head.prev = None
            tempNode.next = None
        elif index == self.length-1:
            tempNode = self.tail
            self.tail = tempNode.prev
            self.tail.next = None
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
            
    
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0
            
            
            
    
newDoubleLL = DoubleLL()
# newDoubleLL.insertFirstNode(5)
newDoubleLL.append(1)
newDoubleLL.append(2)
newDoubleLL.append(3)
newDoubleLL.append(4)
newDoubleLL.append(5)
print(newDoubleLL)
newDoubleLL.prepend(7)
newDoubleLL.prepend(3)
print(newDoubleLL)
newDoubleLL.pop_first()
newDoubleLL.pop_first()
print(newDoubleLL.pop())
print(newDoubleLL.pop())
print(newDoubleLL.insert(34,4))
newDoubleLL.transversal()
print(newDoubleLL.search(6))
print(newDoubleLL.getValue(1))
newDoubleLL.setValue(55,2)
newDoubleLL.remove(0)
newDoubleLL.remove(3)
print(newDoubleLL)