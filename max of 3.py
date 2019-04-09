# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:02:12 2019

@author: Microsoft
"""

a=int(input("ENTER I NUMBER "))
b=int(input("ENTER II NUMBER "))
c=int(input("ENTER III NUMBER "))
if(a>b and a>c):
    print(a)
elif(a>b and a<c):
    print(c)
else:
    print(b)    
