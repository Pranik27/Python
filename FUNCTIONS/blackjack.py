# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:36:19 2020

@author: PRANIKP

BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal 
to 21, return their sum. If their sum exceeds 21 and there's an eleven, 
reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, 
return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19


"""

def blackjack(*args):
    
    new_value = 0
    
    print(args)
    if (sum(args) <= 21):
        return(sum(args))
    elif (sum(args) > 21):
        for i in range(len(args)):
            if(args[i] == 11):
                new_value = sum(args) - 10
                if(new_value <= 21):
                    return (new_value)
        
        return ('BURST')
    
    

value = blackjack(10,10,13) 
print("Sum Value: {}".format(value))