# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:24:50 2023

@author: LAB
"""

year = int(input("type the year: "))
leap = year%4 
if leap ==0 :
    print("this is a leap year")
else:
        print("this is not a leap year")