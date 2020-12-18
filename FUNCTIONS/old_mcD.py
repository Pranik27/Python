# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 23:35:19 2020

@author: PRANIKP


OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald

"""

def old_mcd(st):
    new_str = []
    
    
    for letter in range(3):
        if (letter == 0 or letter == 3):
            new_str.append(st[letter].upper())
        else:
            new_str.append(st[letter])
    
    return ''.join(new_str)

    
     
         
value = old_mcd('macdonald')
print("new Vlaue: {}".format(value))