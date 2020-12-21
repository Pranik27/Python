# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:04:43 2020

@author: PRANIKP

Password Checker
"""

user_name = input("Please enter your user name:")
Password = input("please enter your password:")


print("{}, your {} is {} characters long.".format(user_name,('*' * len(Password)), len(Password)))