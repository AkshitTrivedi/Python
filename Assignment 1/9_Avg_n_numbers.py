# -*- coding: utf-8 -*-
"""
9. Write a program to calculate the average of a set of n given numbers.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

avg=0
n=int(input("How many Elements do you want to Enter: "))

for i in range(n):
    num=int(input("Enter the Value for Element {0}: ".format(i+1)))
    avg=avg+num;
    
print("\nThe Average of {0} Numbers is: {1}".format(n,avg/n))