#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:16:19 2023

@author: palashchaudhari
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = linkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
            
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isEmpty():
            return "There is no any Node in the Queue..."
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
        
    def peek(self):
        if self.isEmpty():
            return "There is no any Node in the Queue..."
        else:
            return self.linkedList.head
            
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
        
        
##########################################Queue LinkedList Module End#######################


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insertBT(rootNode, newNode):
    if rootNode is None:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
               root.value.leftChild = newNode
               return "New node successfully inserted..."
                
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
               root.value.rightChild = newNode
               return "New node successfully inserted..."


                        
newBT = BinaryTree("Drinks")
leftChild = BinaryTree("Hot")
rightChild = BinaryTree("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

leftleftChild = BinaryTree("Tea")
leftrightChild = BinaryTree("Coffee")
rightleftChild = BinaryTree("CocaCoal")
rightrightChild = BinaryTree("Fanta")

leftChild.leftChild = leftleftChild
leftChild.rightChild = leftrightChild
rightChild.leftChild = rightleftChild
rightChild.rightChild = rightrightChild

insertBT(newBT, "India Tea")
