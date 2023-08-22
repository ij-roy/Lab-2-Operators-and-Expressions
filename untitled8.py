# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:34:20 2023

@author: LAB
"""

i = int(input("type a number between 1 to 86400:"))
if i<1 or i>86400:
    print("invalid input")
else:   
     h = i//3600
     j = i%3600
     m = j//60
     s = j%60
     print(h,"hours",m,"minutes",s,"seconds")
