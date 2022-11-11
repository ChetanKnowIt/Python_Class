# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 07:23:56 2022

@author: admin
"""
#assignment11;

print('Hello, {} you are {} yr old and your salary is {}'.format("sandy",21,5000))#default
print('hello %s you are %d and your salary is %f'%("sandeep",21,500002554))
print('Hello, {1} you are {0} yr old and your salary is {2}'.format(21,"sandy",5000))#positional
print('Hello, {name} you are {age} yr old and your salary is {salary}'.format(age=21,name="Akash",salary=5000))#key value formatting
name='Akash'
age=26
print(f"Myname is {name} my age is {age} and salary/month is {25**10}")