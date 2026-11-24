# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:34:09 2026

@author: Sam-Tech
"""

def rotate_right(lst,k):
     if not lst :
         return lst
     
     k = k % len(lst)
     
     rotated = lst[-k:]+lst[:-k]
     return rotated

employees = input().strip().split()
k = int(input().strip())

result =rotate_right(employees, k)
print(" ".join(result))


     