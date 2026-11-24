# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:15:31 2026

@author: Sam-Tech
"""

def print_multipiicatin_table(n):
    for i in range(1,n+1):
        row = []
        for j in range (1, n+1):
            row .append(str(i*j))
        print (" ".join(row))

n=int(input())
print_multipiicatin_table(n)
