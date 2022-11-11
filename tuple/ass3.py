# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:25:56 2022

@author: admin
"""
#1
t1=(1,2,3,4)
t2=(5,6,7,8)
print(t1)
print(t2)
#2
combo=(t2+t1)
print(combo)
#3
t4= list(combo)
t4.sort()
combo2 = tuple(t4)
print(combo2)
#4
print(combo2[2])
#5
print(combo2[-3:])
#6
print(len(combo2))

