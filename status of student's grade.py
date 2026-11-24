# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:08:09 2026

@author: Sam-Tech
"""

mark=int(input("نمره دانش اموز را وارد کنید "))
if mark<0 or mark>20:
    print("نمره باید بین ۱ تا ۲۰باشد")
elif mark<10 :
    print("مردود")
elif 10<mark<15:
    print("قابل قبول")
elif mark>15:
    print("عالیی")