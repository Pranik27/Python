# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 23:48:01 2020

@author: PRANIKP

MASTER YODA: Given a sentence, return a sentence with the words reversed¶
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

"""

def master_yoda(st):
    new_list = st.split()
    print(new_list)
    result = new_list[::-1]
    print(result)
    
    return ' '.join(result)
    

final_string = master_yoda('I am home')
print("Value of final stirng: {}".format(final_string))

final_string = master_yoda('We are ready')
print("Value of final stirng: {}".format(final_string))