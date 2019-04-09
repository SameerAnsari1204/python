# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:45:10 2019

@author: Microsoft
"""
maths=int(input("MATHS= "))
physics=int(input("PHYSICS= "))
chemistry=int(input("CHEMISTRY= "))
english=int(input("ENGLISH= "))
CS=int(input("COMPUTER SCIENCE= "))
total=maths+physics+chemistry+english+CS
print("TOTAL OUT OF 500 - ",total)
percentage=(total/500)*100
print(percentage,"%")
avg=total/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")