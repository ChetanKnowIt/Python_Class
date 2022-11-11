# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:13:32 2022

@author: admin
"""

d = {1:11, 2:22, 3:33, 4:44, 5:55}
print(d)
k = int(input("Enter key: "))

d.pop(k)

print(d)