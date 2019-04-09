# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:05:32 2019

@author: Microsoft
"""

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year",year,"is a leap year!")
else:
    print("The year",year,"isn't a leap year!")