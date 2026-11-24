# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:45:10 2026

@author: Sam-Tech
"""

students=[]
count=0

while True:
    student=input("نام دانش اموز و ساعت ورود را وارد کنید")
    count=count+1
    if student=="end":
        print("تعداد دانش اموزان وارد شده",count-1)
        break
    
    