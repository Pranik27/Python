# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:55:49 2020

@author: PRANIKP

create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.


"""

class Account():
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return ("Account Owner: {} \nAccount balance: {}".format(self.owner,self.balance))
 
        
    def deposit(self,amount):
        self.balance+= amount
        print("Deposit Accepted\n")
    
    def withdraw(self,amount):
        if(amount > self.balance):
            print("Funds unavailable!!")
        else:
            self.balance = self.balance - amount
            print("Withdrawl Accepted!!")

acc = Account('Pranik',100)



print("Owner: {}".format(acc.owner))
print("Avl Balance: {}\n".format(acc.balance))
print("Deposit amount 200: {}".format(acc.deposit(200)))
print("Avl Balance: {}\n".format(acc.balance))
print("Deposit amount 200: {}".format(acc.deposit(300)))
print("Avl Balance: {}\n".format(acc.balance))
print("Withdraw amont 100: {}".format(acc.withdraw(50)))
print("Avl Balance: {}\n".format(acc.balance))
print("Withdraw amont 100: {}".format(acc.withdraw(1000)))
print("Avl Balance: {}\n".format(acc.balance))

print(acc)