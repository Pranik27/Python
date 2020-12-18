# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:12:08 2020

@author: PRANIKP

Write a Python function to check whether a string is pangram or not. 
(Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"


"""

import string

def isparagram(st,alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    inp_st = st.lower()
    inp_st = inp_st.replace(' ','')
    inp_st = set(inp_st)
    return (inp_st == alphaset)
    
print("IS PANGRAM :{}".format(isparagram('Pack my box with five dozen liquor jugs')))