# -*- coding: utf-8 -*-
"""
12(4). Generate the following pattern:
* * * * *
*       *
*       *
*       *
* * * * *

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""

for i in range(0,5):
    for j in range(0,5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()