# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 06:40:18 2022

@author: admin
"""
#ass 9
a=input('Enter String')
count=0
for i in a:
    count=count+1
print(count)
if count>2:
    print(a[:2]+a[-2:])
else:
    print('Empty string')