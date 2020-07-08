# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:24:01 2020

@author: ansar
"""

def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return(n)
    else:
        return(gcd(n,m%n))
        
print(gcd(14,63))        