# -*- coding: utf-8 -*-
"""
12(9). Generate the following pattern:
                1
               232
              34543
             4567654
            567898765
           67890109876
          7890123210987
         890123454321098
        90123456765432109

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""
x=0
for i in range(9):
    print(" "*(10-i),end="")
    for j in range(i+1):
        if (x==9):
            x=0
        else:
            x+=1
        print(x,end="")
    for j in range(i):
        if (x==0):
            x=9
        else:
            x-=1
        print(x,end="")
    print("")