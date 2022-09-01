# -*- coding: utf-8 -*-
"""
2). Write a Python program to get a string made of the first 2 and the last 2 
chars from a given a string. 
Ex Input : beautiful Expected Output : beul

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
str=input("Enter the String: ")
print("Your Entered String is: ",str)
str=str[0:2]+str[-2:]
print("Output with First 2 & Last 2 Chars is: ",str)
