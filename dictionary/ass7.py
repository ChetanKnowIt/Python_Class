# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:27:39 2022

@author: admin

program to map two lists into a dictionary
"""

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
d = dict(zip(l1, l2))
print(d)
