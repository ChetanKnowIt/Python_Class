# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:10:30 2022

@author: admin
"""
#l=list(map(lambda a:a*a,[x for x in range(1,11)]))
#print(l)
def sqr(a):
    return a*a
l=list(map(sqr,[i for i in range(1,11)]))
print(l)