# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 07:07:12 2022

@author: admin
"""
#ass 10
a=input("Enter string ")
print(a)
b=input("Enter Character ")
print(b)
'''c=a[0]
print(c)
if b==c:
    print('String start with same character ')
else:
    print('Not Same')'''
if(a.startswith(b)):
    print('same')
else:
    print('not same')