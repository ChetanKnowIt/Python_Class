# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:14:10 2022

@author: admin
"""
sum =0
n=[4,8,-9,-2,84,66,2,7,-54,21, 99]
pos=[a for a in n if a>0]
evn=[i for i in pos if i%2==0]
print(pos)
print(evn)
for i in evn:
    sum = i+sum
print(sum)
neg=[b for b in n if b<0]
print(neg)
sumneg=0
for i in neg :
    sumneg=i+sumneg
print (sumneg)
odd=[a for a in pos if a%2!=0]
print(odd)
sumod=0
for e in odd :
    sumod=e+sumod
print(sumod)
