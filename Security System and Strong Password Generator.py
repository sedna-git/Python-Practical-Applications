# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:06:55 2026

@author: Sam-Tech
"""

def validate_password(password):
    
    if len(password) < 8:
        return False
    
    has_digit = False
    has_upper = False
    only_digits= True
    
    for char in password:
        if char.isdigit():
            has_digit = True
        else:
            only_digits = False 
        if char.isupper():
            has_upper = True
         
    if has_digit and has_upper and not only_digits:
        return True
    else:
        return False

password = input().strip()

if validate_password(password):
    print("valid")
     
else:
    print("invalid")
    
        