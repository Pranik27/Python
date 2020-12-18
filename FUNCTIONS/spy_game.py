# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 01:38:29 2020

@author: PRANIKP


SPY GAME: Write a function that takes in a list of integers and returns True 
if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
 
 
"""

def spy_game(args):
    
    count = 0
    
    for num in args:
        
        if(num == 0 and count == 0):
            count += 1
        elif(num == 0 and count == 1):
            count += 1
        elif(num == 7 and count == 2):
            return True
        elif(num == 0 and count == 2):
            count =1
    
    return (False)


value = spy_game([1,7,2,0,0,0,7]) 
print("return value : {}".format(value))