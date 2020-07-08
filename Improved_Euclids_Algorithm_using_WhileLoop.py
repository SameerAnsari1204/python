# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:27:08 2020

@author: ansar
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:24:01 2020

@author: ansar
"""

def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    
    while m%n!=0:
       (m,n)=(n,m%n)
    
    return(n)
    
    
print(gcd(14,63))        