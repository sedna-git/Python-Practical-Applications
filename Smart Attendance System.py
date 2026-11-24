# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:21:09 2026

@author: Sam-Tech
"""

def present_students(statuses):
    
    count={}
    
    for status in statuses:
        if status in count :
            count[status] +=1
        else:
            count[status] = 1
                  
    return count

statuses = input().strip().split()

present_students = present_students(statuses)
present = present_students.get('present',0)
absent =  present_students.get('absent',0)

print("present:",present)
print("absent:",absent)