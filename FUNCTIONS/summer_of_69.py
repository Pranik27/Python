# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:50:19 2020

@author: PRANIKP

SUMMER OF '69: Return the sum of the numbers in the array,
 except ignore sections of numbers starting with a 6 and extending to the next 9 
 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14


"""

def summer_69(num_list):
    
    final_sum = 0
    sum_ind = 'Y'
    
    
    for num in range(len(num_list)):
        
        if (num_list[num] == 6):
            sum_ind = 'N'
        elif(num_list[num] == 9):
            sum_ind = 'Y'
            continue
        if (sum_ind == 'Y'):
            final_sum += num_list[num] 

        
    return(final_sum)

result = summer_69([2, 1, 6, 9, 11])
print("RESULT: {}".format(result))