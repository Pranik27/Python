# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:28:36 2020

@author: PRANIKP

Age detector
"""

from datetime import date

def calc_age():
    
    birth_year = float('Inf')
    curr_date = date.today()
    curr_year = int(curr_date.year)
    count = 0
    
    while (birth_year > curr_year):
        
        if count > 0:
            print("Please enter the correct birth year!!!")
            
        birth_year = int(input("In what year where you born?"))
        count += 1
        
    print(curr_year - birth_year)
    

calc_age()