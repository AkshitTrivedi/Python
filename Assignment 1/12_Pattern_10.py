# -*- coding: utf-8 -*-
"""
12(10). Generate the following pattern:
        12345
        1234
        123
        12
        1

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""

for i in range(6,1,-1):                
    for j in range(1,i):        
       print(j,end=" ")  
    print()