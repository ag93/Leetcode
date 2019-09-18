# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:57:34 2019

@author: anike
"""

direction = [1,1,1,0]
amount = [2,1,2,1]

org = 'abcdef'


def leftrotate(string):
    temp = string[0]
    string = string[1:]
    string = string + temp   
    return string 

def rightrotate(string):
    temp = string[-1]
    string = string[:-1]
    string = temp + string
    
    return string

for i in range(len(direction)):
    if(direction[i] == 1):
        for i in range(amount[i]):
            org = rightrotate(org)
    else:
        for i in range(amount[i]):
            org = leftrotate(org)
    
print(org)

