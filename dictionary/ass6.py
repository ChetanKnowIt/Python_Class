# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:20:21 2022

@author: admin
"""

sampleDict = {"name": "Ramu", "age": "25", "state": "Goa"}
print(sampleDict)
# change state to location
sampleDict["location"] = sampleDict.pop("state")
print(sampleDict)
