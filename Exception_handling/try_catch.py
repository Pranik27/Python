# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:31:37 2020

@author: PRANIKP
"""

'''
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
'''

for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print("the input provided is not a number\n")



'''
Problem 2
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

'''
    
x = 5
y = 0

try:
    
    z = x/y
except ZeroDivisionError:
    print("denominator 0 is not accepted\n")
finally:
    print("Provide a proper denominator\n")
    


'''

Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

'''
def ask():
    while True:
        try:
            num = int(input("input an Integer: \n"))
            
        except:
            print("An error occurred! Please try again!\n")
            continue
        else:
            print("Thank you, your number squared is:{}\n".format(num**2))
            break
    
ask() 