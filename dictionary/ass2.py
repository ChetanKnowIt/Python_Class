# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:02:59 2022

@author: admin

concat two dictionaries into one

"""


d = {1:11, 2:22,3:33}
d1 = {5:55, 6:66}

d2 = {**d, **d1}

print(d2)
