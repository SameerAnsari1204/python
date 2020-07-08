# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:50:08 2020

@author: ansar
"""

def gcd(m,n):
    #m should always be greater than n
    if m<n:
        (m,n)=(n,m)
        
    if(m%n==0):
        return(n)
        
    else:
        diff=m-n
        #recursion
        return(gcd(max(n,diff),min(n,diff)))
        
print(gcd(14,63))        