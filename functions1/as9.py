# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:00:22 2022

@author: admin
"""

l1=['r','g','b']
l2=['red','green','blue']
def gendict(l1,l2):
    d=dict(zip(l1,l2))
    return d
print(gendict(l1,l2))