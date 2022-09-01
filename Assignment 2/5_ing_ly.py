# -*- coding: utf-8 -*-
"""
5). Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead. If the string length of the given string is less than 3, leave it 
unchanged.
Ex Input : test Expected Output : testing
 If Input : testing Expected Output: testingly
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
str=input("Enter the String: ")
if len(str)<=3:
    print("Your String: "+str)
elif (str[-3:]=='ing'):
    print("Your String: "+str+'ly')
else:
    print("Your String: "+str+'ing')