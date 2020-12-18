# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:10:15 2020

@author: PRANIKP


FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False


"""
def has_33(val_list):
    
    for i in range(len(val_list) -1):
        
        if(val_list[i] == 3 and val_list[i+1] == 3):
            return True
    return False
        
            

Value = has_33([3, 1, 3])
print("returned value : {}".format(Value))