# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:29:31 2022

@author: admin
"""

n=[7,9,10,5,87,88,96,33,55555,88888,54,753]
odd=[x for x in n if x%2>0]
print(odd)
print(max(odd))
print(n)
evn=[i for i in n if i%2==0]
print(max(evn))
