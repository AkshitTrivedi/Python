# -*- coding: utf-8 -*-
"""
12(8). Generate the following pattern:
    1
    12
    123
    1234
    12345

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""

for i in range(0,6,1):                
    for j in range(1,i+1,1):        
       print(j,end=" ")  
    print()