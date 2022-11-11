# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 06:22:51 2022

@author: admin
"""
#ass7
a="HAmara SANDEEP pyara pyra "
cnt=0
for i in a:
    cnt=cnt+1
print(cnt)

c=0 #uppercase count
b=0 #lowercase count
for i in a:
    if i.isupper():
        c=c+1
    elif i.islower():
        b=b+1
print(c)
print(b)