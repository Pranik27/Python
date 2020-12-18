# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:20:14 2020

@author: PRANIKP

Create a Cylinder Class
"""

class Cylinder():
    
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return(self.pi * self.radius**2 * self.height)
    
    def surface_area(self):
        sur_ar = 2 * self.pi * self.radius  * (self.height + (self.radius))
        return(sur_ar)
    
c= Cylinder(2,3)


area = c.surface_area()

print("Volume of Cylinder: {}\n".format(c.volume()))
print("Area of Cylinder: {}\n".format(area))



########################################################################################
'''
Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

'''

class Line():
    
    def __init__(self,cord1,cord2):
        self.x1,self.y1 = cord1
        self.x2,self.y2 = cord2

    def distance(self):

        dis = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) ** (1/2)
        return(dis)
    
    def slope(self):
        
        slp = (self.y2 - self.y1)/(self.x2 - self.x1)
        return(slp)
    

l = Line((3,2),(8,10))

print("Distance: {}\n".format(l.distance()))
print("SLOPE: {}\n".format(l.slope()))
    
    
    
    
    
    
    
    
    