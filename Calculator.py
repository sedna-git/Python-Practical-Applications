# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:16:57 2026

@author: Sam-Tech
"""

def add(a,b):
    return a+b
def subtract(a,b):
    return a - b 
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0 :
        return "هشدار عدد وارد شده صفر اشت ، عدد دیگری وارد کنید"
    return a / b

a,b = map(float,input().split())
opration = input().strip()

if opration == "+":
    result=add(a,b)
    
elif opration == "-":
    result == subtract(a, b)
    
elif opration == "*":
    result=multiply(a, b)
    
elif opration == "/":
    result =divide(a, b)
else:
    print("علامت ناشناخته!لطفا علامت دیگری وارد کنید")
    
print(int(result))
    


        
        