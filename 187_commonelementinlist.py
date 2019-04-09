# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:30:11 2019

@author: Microsoft
"""

n=int(input("No. of elements in list 1: "))
list1=[]
for i in range(n):
    list1.append(int(input()))
    #print(list1)
q=int(input("No. of elements in list 2: "))
list2=[]
for i in range(q):
    list2.append(int(input()))
    #print(list2)
for x in list1:  
        for y in list2: 
            if x == y: 
                print("True")
            else:
                print("False")