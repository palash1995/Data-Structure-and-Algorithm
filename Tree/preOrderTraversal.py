#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:38:04 2023

@author: palashchaudhari
"""
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
        
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

preOrderTraversal(newBT)


