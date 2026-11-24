# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:34:16 2026

@author: Sam-Tech
"""

def control_scores(scores):
    mean = max(scores) / len(scores) 
    sorted_scores= sorted(scores)
    n = len(sorted_scores)
    if n % 2 == 0 :
        median = (sorted_scores[n//2-1]+sorted_scores[n//2]) /2
    else:
        median = sorted_scores[n//2]
        
    maximum = max(scores)
    
    return mean , median , maximum
scores =list(map(int, input().strip().split()))

mean,median,maximum = control_scores(scores)
print(mean,median,maximum)