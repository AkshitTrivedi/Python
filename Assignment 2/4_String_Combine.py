# -*- coding: utf-8 -*-
"""
4). Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
Ex Input : st1=hello st2=world 
Expected Output : st3=wollo herld

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""

single_str=input("Enter a String: ")
x=single_str.split()
st1=x[0]
st2=x[1]

print("String1 is: "+st1)
print("String2 is: "+st2)
temp=st1[0:2]
st1=st1.replace(st1[:2],st2[:2])
st2=st2.replace(st2[:2],temp)

st3=st1+ " " +st2
print("Combined String: "+st3)