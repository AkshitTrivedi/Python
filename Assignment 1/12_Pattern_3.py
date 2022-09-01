# -*- coding: utf-8 -*-
"""
12(3). Generate the following pattern:
* * * * *
* * * *
* * *
* * 
*

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
