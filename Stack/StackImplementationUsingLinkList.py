#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 02:42:40 2023

@author: palashchaudhari - Palash Chaudhari
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
        
class Stack:
    def __init__(self):
        self.linkedList = LinkedList()
        
    def __str__(self):
        value = [str(x.value) for x in self.linkedList]
        return '\n'.join(value)
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
        
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.linkedList.head
        self.linkedList.head = newNode
        
    def pop(self):
        tempNode = self.linkedList.head
        self.linkedList.head = tempNode.next
        tempNode.next = None
        return tempNode.value
    
    def peek(self):
        if self.linkedList.head == None:
            print("Stack is empty..")
        else:
            # tempNode = self.linkedList.head
            return self.linkedList.head.value
        
    def delete(self):
        self.linkedList.head = None
        print("Stack is deleted..")
        
        
newStack = Stack()

print(newStack.isEmpty())
newStack.push(1)
newStack.push(2)
newStack.push(3)
newStack.push(4)
newStack.push(5)
print(newStack)
print("Push completed")
newStack.pop()
newStack.pop()
print("pop is completed..")
print(newStack.peek())
newStack.delete()
print(newStack)


        
