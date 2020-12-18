# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:56:00 2020

@author: PRANIKP


ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

def animal_crackers(st):
    my_str = st.lower().split()
    out_list = []
    print(my_str)
    
    for word in my_str:
        out_list.append(word[0])
        
        
    if(out_list[0] == out_list[1]):
        return True
    
    return False
    
value = animal_crackers('Crazy Kangaroo') 
print("value retunred: {}".format(value))