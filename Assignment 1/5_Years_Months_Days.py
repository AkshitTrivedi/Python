# -*- coding: utf-8 -*-
"""
5. Write a program to accept number of days and print year, month and 
remaining days.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

days=int(input("Enter Days: "))

years = (days // 365)
months = (days - years * 365) // 30
rem_days = (days - years * 365 - months * 30)

print("Years:",years)
print("Months:",months)
print("Days:",rem_days)