# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:41:45 2020

@author: PRANIKP
"""

class Animal:
    
    def __init__(self,type):
        self.type = type
        print("This is Animal Class")
        
    def animalType(self):
        print("Animal type is", self.type)
        

class Dog(Animal):
    
    def __init__(self):
        super().__init__("Non Mammal")
        print("This is Dog class")
        
        
    def dogAttr(self):
        print("Dog can bark")
        print("Calling Animal class Method")
        super().animalType()

class Cat(Dog):
    
    def __init__(self):
        
        print("This is Cat class")
        super().__init__()
        
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

print(issubclass(Cat,Animal)) 
print(isinstance(a,Animal))

        
    