#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 01:38:25 2023

@author: palashchaudhari
"""

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is Full..."
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "Node inserted successfully..."
    
    def searchBT(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Data Found..."
        return "Data Not Found..."
    
    def preOrderTraversal(self, index):
        if index == 0:
            index +=1
        if index > self.lastUsedIndex:
            return "Node Not Found..."
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal((index*2)+1)
        
    def inOrderTraversal(self, index):
        if index == 0:
            index +=1
        if index > self.lastUsedIndex:
            return "Node Not Found..."
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal((index*2)+1)
        
    def postOrderTraversal(self, index):
        if index == 0:
            index +=1
        if index > self.lastUsedIndex:
            return "Node Not Found..."
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        if index == 0:
            index +=1
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
            
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "Unable to Proceed..."
        for i in range(1, self.lastUsedIndex):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                
    def deleteBT(self):
        self.customList = None
        return "Binary Tree Delete Successfully..."
                
    def printBT(self):
        print(self.customList)
    
newBT = BinaryTree(8)
print(newBT.insertNode("Drink"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print(newBT.insertNode("CocaCola"))
print(newBT.insertNode("Boba"))
print(newBT.searchBT("Boba"))
newBT.preOrderTraversal(0)
newBT.inOrderTraversal(0)
newBT.postOrderTraversal(0)
newBT.levelOrderTraversal(1)
newBT.printBT()
newBT.deleteNode("Cold")
newBT.printBT()
newBT.deleteBT()
newBT.printBT()