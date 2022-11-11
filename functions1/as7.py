# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:30:45 2022

@author: admin
def findunique(lst):
    lst1 = list(dict.fromkeys(lst))
    return lst1
    
"""



def findunique(lst):
    l2=list(set(lst))
    return l2

lst = [1,2,3,3,3,4,5]
newlist = findunique(lst)
print(newlist)
    
