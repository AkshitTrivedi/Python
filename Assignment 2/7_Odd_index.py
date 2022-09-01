# -*- coding: utf-8 -*-
"""
7). Write a Python program to remove the characters which have odd index 
values of a given string.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""

str=input("Enter the String: ")
print("Your Entered String: "+str)
odd=str[1::+2]
print("String with odd Index: "+odd)