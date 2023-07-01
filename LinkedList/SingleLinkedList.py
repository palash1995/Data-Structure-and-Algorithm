#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 19:53:33 2023

@author: palashchaudhari
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result = result+" -> "
            tempNode = tempNode.next
        return result
        
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1
        
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1
            
    def insert(self, value, index):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if index == 0:
                newNode.next = self.head
                self.head = newNode
            else:
                tempNode = self.head
                for _ in range(index-1):
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                tempNode.next = newNode
        self.length +=1
                
    def transveral(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
            
    def search(self, target):
        currNode = self.head
        index=0
        while currNode:
            if currNode.value == target:
                return index
            index += 1
            currNode = currNode.next
        return -1
    
    def getValue(self, index):
        currNode = self.head
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return False
        for _ in range(index):
            currNode = currNode.next
        return currNode
    
    # def setValue(self, value, index):
    #     currNode = self.head
    #     if index == -1:
    #         self.tail.value = value
    #     if index < 1 or index >= self.length:
    #         return False
    #     for _ in range(index):
    #         currNode = currNode.next
    #     currNode.value = value
    
    def setValue(self, value, index):
        currNode = self.getValue(index)
        while currNode:
            currNode.value = value
            return
        return False
    
    def pop_first(self):
        currNode = self.head
        self.head = currNode.next
        currNode.next = None
        self.length -= 1
        return currNode.value
    
    def pop(self):
        currNode = self.head
        tempNode = self.tail
        while currNode.next is not self.tail:
            currNode = currNode.next
        self.tail = currNode
        currNode.next = None
        self.length -= 1
        return tempNode.value
    
    def remove(self, index):
        if index == 0:
            tempNode = self.head
            self.head = tempNode.next
            tempNode.next = None
        else:
            prevNode = self.getValue(index-1)
            tempNode = prevNode.next
            prevNode.next = tempNode.next
            tempNode.next = None
        return tempNode.value
    
    def delete(self):
        self.head = None
        self.tail = None
        self.lenght = 0
        


newLL = LinkedList()
newLL.prepend(1)
newLL.append(2)
newLL.append(3)
newLL.append(4)
newLL.append(5)
newLL.insert(6,0)
newLL.insert(9,1)
print(newLL)
# newLL.transveral()
# print(newLL.search(2))
# print(newLL.getValue(-1))
# newLL.setValue(28,9)
# print(newLL)
#print(newLL.pop_first())
# print(newLL.pop_first())
# print(newLL.pop_first())
print(newLL.pop())
print(newLL.pop())
print(newLL.pop())
print(newLL.pop())
# print(newLL.remove(0))
# newLL.delete()
print(newLL)







# print(newLL.head)
# print(newLL.tail)
# print(newLL.head.value)
# print(newLL.head.next)
# print(newLL.head.next.value)
# print(newLL.head.next.next.value)