# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:09:09 2019

@author: Microsoft
"""

month_name = input("Input the name or number of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 