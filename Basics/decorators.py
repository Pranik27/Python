# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 00:53:13 2021

@author: PRANIKP



Time Complexity:
Space Complexity:
"""

# Create an @authenticated decorator that only allows the function to run is user1 has 
#'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
  def wrap_func(*args,**kargs):
      for item in args:
          if (item['valid']):
              fn(*args,**kargs)
  return wrap_func

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)