# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:44:37 2020

@author: PRANIKP
"""
"""

LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
if both numbers are even, but returns the greater if one or both numbers are odd

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5

"""
def lesser_of_two_evens(num1,num2):
    if (num1%2 == 0 and num2%2 == 0):
        if (num1 > num2):
            return num2
        else:
            return num1
    else:
        if (num1 > num2):
            return num1
        else:
            return num2
    
value = lesser_of_two_evens(2,4)
print("Number Returned: {}".format(value))
value = lesser_of_two_evens(2,5)
print("Number Returned: {}".format(value))