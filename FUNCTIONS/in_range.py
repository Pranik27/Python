# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:30:29 2020

@author: PRANIKP

Write a function that checks whether a number is in a given range 
(inclusive of high and low)

ran_check(5,2,7)

"""

def ran_check(num,low,high):
    if (low <= num <= high):
        return True
    return False

val = ran_check(11,2,7)
print("in Range : {}".format(val))