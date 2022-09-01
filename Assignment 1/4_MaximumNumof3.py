# -*- coding: utf-8 -*-
"""
4. Write a program to determine the maximum of 3 numbers.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

num1=float(input("Enter Num1: "))
num2=float(input("Enter Num2: "))
num3=float(input("Enter Num3: "))

if(num1>=num2) and (num1>=num3):
    print("\n{0} is the Greatest of all Numbers.".format(num1))
elif(num2>=num3) and (num2>=num1):
    print("\n{0} is the Greatest of all Numbers.".format(num2))
else:
    print("\n{0} is the Greatest of all Numbers.".format(num3))
