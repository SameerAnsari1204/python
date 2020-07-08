# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:20:20 2020

@author: ansar
"""

def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if(m%i==0) and (n%i==0):
            cf.append(i)
            
    return(cf[-1])    
        
print(gcd(14,63))        