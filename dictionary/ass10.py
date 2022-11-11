# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:58:22 2022

@author: admin
"""

people={'arhan':'blue','monica':'red','lisa':'yellow','vinod':'purple','jenny':'pink'}
numof_people =len(people)
print(numof_people)
people.update({'lisa':'orange'})
print(people)
a=people.pop('lisa')
n=sorted(people.keys())
for i in n:
    print(i, people[i])