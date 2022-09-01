# -*- coding: utf-8 -*-
"""
3). Write a Python program to get a string from a given string where all 
occurrences of its first char have been changed to '$', except the first char 
itself.
Ex Input : abracadabra Expected Output : abr$c$d$br$

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""

str=input("Enter the String: ")
char=str[0]
str=str.replace(char, '$')
str=char+str[1:]
print("String with $: "+str)
