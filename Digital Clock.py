# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:19:57 2026

@author: Sam-Tech
"""
def add_minutes(hours,minutes,extra_minutes):
    
    
    total_minutes= hours*60 + minutes + extra_minutes
    new_hours = int(total_minutes /60) % 24
    new_minutes = total_minutes % 60
    
    return new_hours , new_minutes


hours,minutes = map(int,input().strip().split())
extra = int(input())

new_hours , new_minutes = add_minutes(hours,minutes,extra)
print({new_hours},":",{new_minutes})

