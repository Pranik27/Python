# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:49:33 2020

@author: PRANIKP


Write a Python function that takes a list and returns a new list with unique elements 
of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

"""

def unique_list(inp_list):
    return(list(set(inp_list)))


    
out_list = unique_list([1, 89, 1, 1, 2, 73, 3, 3, 3, 3, 4, 5])
print("New list: {}".format(out_list))