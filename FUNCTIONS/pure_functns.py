# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 18:17:46 2021

@author: PRANIKP



Time Complexity:
Space Complexity:
"""

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capiltalize_pet(items):
    return items.upper()

print(list(map(capiltalize_pet,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()

print(list(zip(my_strings,my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def valid_score(item):
    return item > 50

print(list(filter(valid_score,scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulate(acc,item):
    return acc + item

print(reduce(accumulate,my_numbers+scores,0))


    
    
