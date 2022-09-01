# -*- coding: utf-8 -*-
"""
7. Admission to a professional course is subject to the following conditions :
(a) marks in mathematics >= 60
(b) marks in physics >= 50
(c) marks in chemistry >= 40
(d) total in all three subjects >= 200
or
 total in mathematics and physics >= 150
 given the marks in the three subjects , write a program to 
process the applications to list an eligible candidate.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

math=int(input("Enter Marks of Mathematics: "))
phy=int(input("Enter Marks of Physics: "))
chem=int(input("Enter Marks of Chemistry: "))

tot=math+phy+chem
pm=phy+math

if(math>=60 and phy>=50 and chem>=40 and (tot>=200 or pm>=150)):
    print("\nStudent is Eligible")
else:
    print("\nStudent is not Eligible")
