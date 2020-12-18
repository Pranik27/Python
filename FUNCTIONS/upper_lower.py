# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:37:51 2020

@author: PRANIKP

Write a Python function that accepts a string and calculates the number of upper case
letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33


"""

def up_low(st):
    my_list = st.split()
    upper_count = 0
    lower_count = 0
    print(my_list)
    
    for word in my_list:
        for i in range(len(word)):
            if(word[i].isupper()):
                upper_count += 1
            elif(word[i].islower()):
                lower_count += 1
    return(upper_count,lower_count)
                
    

up_count,low_count = up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print("upper count : {} , lower count : {}".format(up_count,low_count))