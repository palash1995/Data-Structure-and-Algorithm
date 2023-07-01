#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 00:30:10 2023

@author: palashchaudhari
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CSLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode:
            result += str(tempNode.value)
            if tempNode.next == self.head:
                break
            if tempNode.next is not None:
                result = result+" -> "
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
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        self.length += 1
        
    def insert(self, value, index):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            if index == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            else:
                tempNode = self.head
                for _ in range(index-1):
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                tempNode.next = newNode
        self.length += 1
        
    def transverse(self):
        tempNode = self.head
        while tempNode.next is not self.head:
            print(tempNode.value)
            tempNode = tempNode.next
            
    def search(self, target):
        index=0
        tempNode = self.head
        while tempNode.next is not self.head:
            if tempNode.value == target:
                return index
            index+=1 
            tempNode = tempNode.next
        return False
    
    # def get_value(self, index):
    #     print(self.length)
    #     tempNode = self.head
    #     for i in range(self.length-1):
    #         if i == index:
    #             return tempNode
    #         tempNode = tempNode.next
    #     return "Invalid index"
    
    def get_value(self, index):
        tempNode = self.head
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return False
        else:
            for _ in range(index):
                tempNode = tempNode.next
            return tempNode
    
    def set_value(self, value, index):
        index = self.get_value(index)
        if index is False:
            return False
        else:
            index.value = value
            
    def pop_first(self):
        tempNode = self.head
        self.head = tempNode.next
        self.tail.next = self.head
        tempNode.next = None
        self.length -= 1
        return tempNode.value
    
    def pop(self):
        currNode = self.head
        tempNode = self.tail
        while currNode.next is not self.tail:
            currNode = currNode.next
        self.tail = currNode
        currNode.next = self.head
        tempNode.next = None
        self.length -= 1
        return tempNode.value
    
    def remove(self, index):
        if index == 0:
            tempNode = self.head
            self.head = tempNode.next
            self.tail.next = self.head
            tempNode.next = None
        else:
            prevNode = self.get_value(index-1)
            tempNode = prevNode.next
            prevNode.next = tempNode.next
            tempNode.next = None
        self.length -= 1
        return tempNode.value
    
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    
        
        
newCSLL = CSLinkList()
newCSLL.append(1)
newCSLL.append(2)
newCSLL.append(3)
newCSLL.append(4)
newCSLL.append(5)
newCSLL.append(6)
print(newCSLL)
newCSLL.insert(98,3)
print(newCSLL)
print(newCSLL.search(5))
print(newCSLL)
print(newCSLL.set_value(77,9))
print(newCSLL.pop_first())
print(newCSLL.pop())
print(newCSLL.pop())
print(newCSLL.remove(2))
newCSLL.delete()

print(newCSLL)


        