# -*- coding: utf-8 -*-
"""
9). Write a Python program to get the second largest number from a list.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
lst=[]
n=int(input("How many elements you want to Enter: "))

for i in range(0,n):
    ele=int(input("Enter the Element {0}: ".format(i+1)))
    lst.append(ele)
print("\nEntered List is: ",lst)
lst.sort()
print("\nSorted List is: ",lst)
print("\n2nd Largest Number is: ",lst[-2])
#print("\n2nd Largest Number is: ",sorted(lst)[-2])