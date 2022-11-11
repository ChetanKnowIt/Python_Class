# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:29:14 2022

@author: admin

menu driven program to 

1. add
2. update
3. display
4. find
5. del
"""

d = {}

option = 1
while option:
    print("1. add to dictionary")
    print("2. update dictionary")
    print("3. display dictionary")
    print("4. find in dictionary")
    print("5. delete from dictionary")
    print("6. exit")
    choice = int(input("Enter your option: "))
    
    if choice==1:
        key = int(input("Enter your key"))
        value = int(input("Enter your value"))
        d[key] = value
        print(d)
        
    if choice==2:
        key = int(input("Enter your key"))
        value = int(input("Enter your value"))
        d.update({key:value})
        print(d)
        
    if choice==3:
        print(d)
    if choice==4:
        key = int(input("Enter your key"))
        for i,j in d.items():
            if i==key:
                print(i,d[i])
            if j==key:
                print(i,d[i])
        
    if choice==5:
        print(d)
        key = int(input("Enter your key"))
        del d[key]
        print(d)
        
    if choice==6:
        option=False
    
        
        
        
