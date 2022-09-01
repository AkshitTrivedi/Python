# -*- coding: utf-8 -*-
"""
10). Write a program to remove all the duplicate elements from list.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
lst=[]
n=int(input("How many elements you want to Enter: "))

for i in range(0,n):
    ele=int(input("Enter the Element {0}: ".format(i+1)))
    lst.append(ele)
lst.sort()
print("\nEntered List is: ",lst)
list1=list(set(lst))
list1.sort()
print("\nThe List after removing all the duplicates: ",list1)
