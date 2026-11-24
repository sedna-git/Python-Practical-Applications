# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:17:36 2026

@author: Sam-Tech
"""

def secend_max_score(scores):
    if len(numbers)< 2 :
        return None
    
    largest = float('-inf')
    second_score = float ('-inf')
    
    for num in numbers:
        if num > largest:
            seconed_largest = largest 
            largest = num 
        elif num >second_largest and num!=largest:
            second_score = num
    return secend_largest

numbers= list(map(int , input().strip().split()))

result = secend_max_score(scores)
print(result)
                 

        
    