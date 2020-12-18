# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:19:16 2020

@author: PRANIKP

PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


"""

def paper_doll(st):
    
    my_str = []
    
    for letter in range(len(st)):
        my_str.append(st[letter]*3)
        
    return ''.join(my_str)

final_str = paper_doll('Mississippi') 
print("Final String : {}".format(final_str))
        