# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:56:25 2022

@author: admin
"""
# function to find the longest
# length in the list
def longestLength(a):
	max1 = len(a[0])
	temp = a[0]

	# for loop to traverse the list
	for i in a:
		if(len(i) > max1):

			max1 = len(i)
			temp = i

	print("The word with the longest length is:", temp,
		" and length is ", max1)


# Driver Program
a = ["one", "two", "third", "four"]
longestLength(a)
