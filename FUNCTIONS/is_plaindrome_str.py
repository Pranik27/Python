# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:43:23 2020

@author: PRANIKP

Write a Python function that checks whether a word or phrase is palindrome or not.
"""

def palindrome_str(st):
    replaced_str = st.replace(' ', '')
    
    return (replaced_str[::-1] == replaced_str)
    
    
print("IS PALINDROME STR: {}".format(palindrome_str('nurses run')))