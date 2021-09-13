# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 16:05:52 2021

@author: PRANIKP



Time Complexity:
Space Complexity:
"""

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('c1',10)
cat2 = Cat('c2',20)
cat3 = Cat('c3',30)

allAge = []
allAge.append(cat1.age)
allAge.append(cat2.age)
allAge.append(cat3.age)

# 2 Create a function that finds the oldest cat
def find_oldest(age):
    return max(age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest cat is {} years old.".format(find_oldest(allAge)))