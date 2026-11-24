# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:52:22 2026

@author: Sam-Tech
 """
def get_phone_numbers():
    
    numbers = []
    
    while  True:
        try:
            num = int(input())
            if num == 0:
                break
            numbers.append(num)
        except:
                break
            
    return numbers
numbers = get_phone_numbers()
numbers.reverse()
for num in numbers :
    print(num)
        
            
         
         
    
    
      