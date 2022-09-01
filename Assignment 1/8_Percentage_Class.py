# -*- coding: utf-8 -*-
"""
8. Write a program that reads the percentage obtained by the students and determines and prints the class obtained by the student as per the 
following rules 
                       Percentage       Class
                       0 - 39           Fail
                       40 - 59          Second class
                       60 - 79          First class
                       80 - 100         Distinction
                       
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

name=input("Enter Your Name: ")
per=int(input("Enter your Percentage: "))

if(per>=0 and per<=39):
    print("Student {name} is Fail. Better Luck Next Time!".format(name=name))
elif(per>=40 and per<=59):
    print("Student {name} has got Second Class.".format(name=name))
elif(per>=60 and per<=79):
    print("Student {name} has got First Class.".format(name=name))
elif(per>=80 and per<=100):
    print("Student {name} has got Distinction.".format(name=name))    
