# -*- coding: utf-8 -*-
"""
12(5). Generate the following pattern:
 * * * * *
   * * * *
     * * *
       * *
         *

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""

for i in range(0,5):
    for j in range(0,i+1):        
       print(" ",end=" ")
       
    for k in range(0,5-i):
        print("*",end=" ")
       
    print()