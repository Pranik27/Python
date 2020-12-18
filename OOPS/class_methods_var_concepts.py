# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 04:36:03 2020

@author: PRANIKP
"""

#Class
class Student:
    
    
    school = 'DAV' #Class/Static Variable
    
    def __init__(self,name,roll_no): #Init Method which serves as constuctors in Python
        self.name = name             #All these variables are the instance Variables
        self.roll_no = roll_no
        self.lap = self.Laptop()     #Instantiating the inner class
        
    def get_name(self):             #Instance Method : Accessors
        print(self.name)
        
    def updte_roll(self,value):     #Instance Method : Mutators
        self.roll_no = value
        
    def show(self):                 #Instance Method
        print(self.name,self.roll_no,self.school)
        self.lap.show()
    
    #Below 2 decorators are self explanatory
    @classmethod
    def getschool(cls):
        print(cls.school)
        
    @staticmethod
    def info():
        print("This is the call for student clas ABC")
    
    #Inner class
    class Laptop:
        
        def __init__(self,brand = 'HP',color = 'BLACK'):
            self.brand = brand
            self.color = color
        
        def show(self):
            print(self.brand,self.color)
  
#Objects
s1 = Student('Pranik',2)
s2 = Student('Rahul',5)

s1.show()
s2.show()

s1.get_name()
s2.get_name()

s1.updte_roll(98)
s1.show()


lap1 = Student.Laptop('DELL','WHITE')
lap1.show()

print(Student.school)
Student.getschool()

s1.info()    
Student.info()