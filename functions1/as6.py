# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:49:38 2022

@author: admin
"""

def makelist():
    '''make list for even numbers between 4 to 30 using list comprehension'''
    lst = [x for x in range(4,31) if x%2==0]
    return lst


print(makelist.__doc__)
print(makelist())