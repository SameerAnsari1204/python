# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:00:37 2020

@author: ansar
"""

def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m%i==0):
            fm.append(i)
    
    fn=[]
    for j in range(1,n+1):
        if(n%j==0):
            fn.append(j)
            
    fc=[]
    for c in fm:
        if c in fn:
            fc.append(c)
    
    return(fc[-1])        
    
print(gcd(14,63))    