# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:55:38 2020

@author: ansar
"""

def gcd(m,n):
    #m should always be greater than n
    if m<n:
        (m,n)=(n,m)
        
    while (m%n)!=0:
        diff=m-n
        
        (m,n)=(max(n,diff),min(n,diff))
    return(n)
        
print(gcd(14,63))        