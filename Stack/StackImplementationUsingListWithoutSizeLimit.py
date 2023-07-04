#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:07:37 2023

@author: palashchaudhari
"""
class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        #print(self.list)
        values = self.list.reverse()
        # self.list.reverse()
        # values = []
        #print(self.list)
        #print(values)
        values = [str(x) for x in self.list]
        #print(values)
        return  '\n'.join(values)
    
    # def __str__(self):
    #     print(self.list)
    #     if self.list == []:
    #         return "Stack is empty"
    #     else:
    #         #print(self.list)
    #         values = self.list.reverse()
    #         # self.list.reverse()
    #         # values = []
    #         #print(self.list)
    #         #print(values)
    #         values = [str(x) for x in self.list]
    #         #print(values)
    #         return  '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "Data is pushed into stack"
    
    def pop(self):
        if self.list == []:
            return "Stack is empty. No data to pop!"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.list == []:
            return "Stack is empty. No data to pop!"
        else:
            return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None
    

newStack = Stack()
newStack.isEmpty()
newStack.push(1)
newStack.push(2)
newStack.push(3)
newStack.push(4)
#print(newStack.peek())
print(newStack)
newStack.pop()


