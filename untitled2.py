# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:00:23 2023

@author: LAB
"""
x = int(input("value of x is: "))
y = int(input("value of y is: "))
if x<0 or y<0:
    print("invalid input")
else:
    rem = y%x
    if rem == 0:
        print(y,"is divisible by",x)
    else:
        print(y,"is not divisible by ",x)
        
    
 