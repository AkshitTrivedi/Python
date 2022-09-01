# -*- coding: utf-8 -*-
"""
6. Write a program to swap the values of two variables.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

num1=float(input("Enter Value of 1st Number: "))
num2=float(input("Enter Value of 2nd Number: "))

print("\n\nValue Before Swapping: ")
print("\nValue of 1st Number: ",num1)
print("Value of 2nd Number: ",num2)

num1,num2=num2,num1

print("\n\nValue After Swapping: ")
print("\nValue of 1st Number: ",num1)
print("Value of 2nd Number: ",num2)