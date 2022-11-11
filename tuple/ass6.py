# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:01:31 2022

@author: admin
"""


t=("hello",45,"my wahayk","dfjhj",787,"aksan", (1,2,4,5), ['a','c','v','f'])
n = input('Enter value to search: ')

if n.isdigit():
    n = int(n)
if type(n)==tuple:
    n = int()

if t.count(n)>0:
    print("Found")
else:
    print("not found")

