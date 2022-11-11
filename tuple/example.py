# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:06:28 2022

@author: admin
"""

d = { 2:10, 6:20, 5:3, 3:60}

for i,y in d.items():
    if(y==20):
        d.update({6:60})
        print(d)
        break
    

        
        