# -*- coding: utf-8 -*-
"""
3. Write a program to tell if a year is a leap year Or Not.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

year=int(input("Enter Year to check: "))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))