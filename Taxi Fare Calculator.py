# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:14:34 2026

@author: Sam-Tech
"""

def taxi_kilometers(distance):
     
    if distance <= 3 :
        fare= 15000
    elif distance <= 10:
        fare= (distance*4000)
    else:
        fare= (distance*3000)
        
        return fare
    
distance= int(input("عدد محاسبه شده توسط کیلومتر شمار را وارد کنید "))
fare=taxi_kilometers(distance)
print(fare)