#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:08:47 2023

@author: palashchaudhari
"""

class Graph:
    def __init__(self):
        self.adjenctList = {}
        
    def addVertex(self,vertex):
        if vertex not in self.adjenctList.keys():
            self.adjenctList[vertex] = []
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjenctList:
            print(vertex, ":" , self.adjenctList[vertex])
            
graph = Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.printGraph()

                       