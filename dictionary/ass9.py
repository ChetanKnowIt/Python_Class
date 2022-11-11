# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:48:47 2022

@author: admin
"""
print("------------------------------------")
#1 telephone dict
tdict = {"Madhura Kale": 9911377882,"Ram Kulkarni": 8811299332, "Ram Londhe": 6633199442}
print(tdict)
print("------------------------------------")
#2 change madhura's no to 9155510245
tdict["Madhura Kale"] = 9155510245
print(tdict)
print("------------------------------------")
#3 new entry
tdict.update({"Ankita Deshpande": 985532375})
print(tdict)
print("------------------------------------")
#4 print ram's number
print(tdict["Ram Kulkarni"])
print(tdict)
print("------------------------------------")
#5 print None of name doesn't exist
print(tdict.get("Madhura"))
print("------------------------------------")
#6 print all keys
print("------------------------------------")
for i in tdict.keys():
    print(i)
    
#7 print all values
print("------------------------------------")
for i in tdict.values():
    print(i)
