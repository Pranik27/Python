# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:00:11 2020

@author: PRANIKP

ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

"""

def almost_there(num):
    if (abs(100 -num) <=10 or abs(200 - num) <= 10):
        return True
    else:
        return False
    
result = almost_there(211)
print("vales returned: {}".format(result))

    