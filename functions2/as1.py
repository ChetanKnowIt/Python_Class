# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:51:07 2022

@author: admin
"""

def overlapping(l1, l2):
    for i in l1:
        if i in l2:
            return True
    else:
        return False
            
        
l1 = [1,2,3,4,5]
l2 = [2,8,6,4]
l3 = [22,22,22,22]
print(overlapping(l1,l2))
print(overlapping(l1, l3))

print(dir(__builtins__))
