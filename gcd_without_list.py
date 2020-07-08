# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:27:04 2020

@author: ansar
"""

def gcd(m,n):
    
    for i in range(1,min(m,n)+1):
        if(m%i==0) and (n%i==0):
            cf=i
            
    return(cf)    
        
print(gcd(14,63)) 