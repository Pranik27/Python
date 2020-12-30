# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:46:59 2020

@author: PRANIKP

#Display the image below to the right hand side where the 0 is going to be ' ', 
and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

Time Complexity:O(m*n) where m and n are the no of rows and columns in the matrix
Space Complexity:constant space
"""

class Solution:
    
    def display(self,picture):
        
        for _ in range(len(picture)):
            
            for x in range(len(picture[_])):
                
                if picture[_][x] == 0:
                    print(" ",end='')
                else:
                    print("*",end='')
            print()


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

s = Solution()
s.display(picture)