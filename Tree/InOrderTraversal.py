#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:34:27 2023

@author: palashchaudhari
"""

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
        
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

inOrderTraversal(newBT)