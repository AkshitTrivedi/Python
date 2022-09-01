# -*- coding: utf-8 -*-
"""
 12. Write a Python program to concatenate following dictionaries to create a
     new one.
     d1={1:100, 2:200}
     d2={3:300, 4:400}
     d3={5:500, 6:600}
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
d1={1:100, 2:200}
d2={3:300, 4:400}
d3={5:500, 6:600}
d4={}

for ele in (d1,d2,d3):
    d4.update(ele)

print("New Dictionary is: ",d4)