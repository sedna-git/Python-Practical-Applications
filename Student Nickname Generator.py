# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:13:46 2026

@author: Sam-Tech
"""
first_names = input().split()
nick_names = input() .split()

names=[]

for first in first_names:
    for nick in nick_names:
        names.append(first+ " " +nick)
        
names.sort(key=len)

for name in names:
    print(name)

        
 
