# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:02:21 2020

@author: PRANIKP

Check duplicates in a List
some_list = ['a','b','c','b','d','n','n']
output = {'b','n'} , order of output doesn't matter

Time Complexity: O(n) , where  n is the lenght of the list
Space Complexity: Constant space if output set is not conidered as extra space else O(n)
"""


class Solution:
    
    def checkDuplicate(self,inp_list):
        
        res = set()
        char_count = [0] * 26
        
        
        for item in inp_list:
            
            if char_count[ord(item) - ord('a')] > 0:
                res.add(item)
            else:
                char_count[ord(item) - ord('a')] += 1
        
        return res
    
some_list = ['a','b','c','b','d','n','n']
s= Solution()
print(s.checkDuplicate(some_list))