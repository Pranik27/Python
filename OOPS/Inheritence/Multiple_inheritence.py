# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:35:10 2020

@author: PRANIKP
"""

class Animal:
    
    def __init__(self,type):
        self.type = type
        print("This is Animal Class")
        
    def animalType(self):
        print("Animal type is", self.type)
        

class Dog():
    
    def __init__(self):
        
        print("This is Dog class")
        
        
    def dogAttr(self):
        print("Dog can bark")
     

class Cat(Animal,Dog): #MRO - Method Resolution Order
    
    def __init__(self):
        
        print("This is Cat class")
        super().__init__(" Non Mammal")
        
    def CatAttr(self):
        print("Cat drinks Milk")

        
        
#Single level Inheritence
a = Animal("mammal")
a.animalType()

d = Dog()

d.dogAttr()

#Multi - Level Inheritence

c = Cat()
c.CatAttr()
c.animalType()
c.dogAttr()

print(issubclass(Cat,Dog))

        
    