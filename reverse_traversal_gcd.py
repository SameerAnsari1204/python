# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:31:40 2020

@author: ansar
"""

def gcd(m,n):
    i=min(m,n)
    while i>0:
        if(m%i==0) and (n%i==0):
            return(i)
        else:
            i=i-1
            
print(gcd(14,63))            