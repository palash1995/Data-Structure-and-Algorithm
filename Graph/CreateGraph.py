#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 00:26:54 2023

@author: palashchaudhari
"""

class Graph:
    def __init__(self, gdict=None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict
        
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
        
dict = { "a" : ["b","c"],
          "b" : ["a","d","e"],
          "c" : ["a","e"],
          "d" : ["b","e","f"],
          "e" : ["d","f"],
          "f" : ["d","e"]
        }

graph = Graph(dict)
graph.addEdge
print(graph.gdict)