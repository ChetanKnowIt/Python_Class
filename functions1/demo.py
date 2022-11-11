# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:50:40 2022

@author: Chetan A
############################################################################

                            LAB DEMO EXAMPLES

############################################################################"""

lst = ["hi1","hello1","welcome1"]
lst3 = list(map(lambda s:lst.index(s)%2==0, lst))
print(lst3)


lst = ["hi1","hello1","welcome1"]
lst3 = list(map(lambda s:s[::-1][::2], lst))
print(lst3)


a,b,c = map(int, input("Enter 3 numbers: ").split())
print(a,b,c)



def Positive(a):
    return a>0


l1 = [1, -3, 5, 6, -4, 6, -2]
l2 = list(filter(Positive, l1))
print(l2)

#using lambda
l3 = list(filter(lambda a: a>0, l1))
print(l3)


lst = ["hi1", "hello2", "welcome1", "we","welcome1welcome1"]
l2 = list(filter(lambda a:len(a)>3, lst))
print(l2)



lst = ["hi1", "hello2", "welcome1", "we?","welcome1welcome1"]
l2 = list(filter(str.isalnum, lst))
print(len(l2))

# Example of characters that are not alphanumeric: (space)!#%&? etc.

