# -*- coding: utf-8 -*-
"""
11. Write a program that accept basic, HRA, and DA from the user and 
calculate total salary.

 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""

basic =float(input(" Enter Basic Salary : "))   
p_hra =float(input(" Enter HRA in Percentage (%) : "))       
p_da =float(input(" Enter DA in Percentage (%) : "))       
  
hra = (basic * p_hra)/100  
da  = (basic * p_da)/100  
 
gs  = basic + hra + da  
  
print(" \nGross Salary is: {0:.2f} ₹".format(gs)); 