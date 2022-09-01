# -*- coding: utf-8 -*-
"""
6). Write a Python program to remove the nth index character from a 
nonempty string.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
str=input("Enter the String: ")
print("Your Entered String: "+str)
n=int(input("Enter Index: "))
first=str[0:n]
last=str[n+1:]
str=first+last
print("\nString after removing {0}th Index is: {1}".format(n,str))
