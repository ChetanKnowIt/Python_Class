# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:37:33 2022

@author: admin
"""

l=[1,5,3]
print(list(map(lambda a: (a*a,a**3),[x for x in range(2, 101) if all(x % y != 0 for y in range(2, x))])))



l = [ x for x in range(2,101) if all(x % y!=0 for y in range(2,x))]
print(l)