# -*- coding: utf-8 -*-
"""
1. Write a program to add, multiply and divide two integers and float numbers.

Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22
"""

# print("Program to add, multiply and divide two integers and float numbers.")

# ch = input("Enter 1 for Integer and 2 for Float: ")

# if ch=='1':
#     num1 = int(input("Enter First Integer Number: "))
#     num2 = int(input("Enter Second Integer Number: "))
    
# elif ch=='2':
#     num1 = float(input("Enter First Float Number: "))
#     num2 = float(input("Enter Second Float Number: "))  

# else:
#     print("Invalid Choice: ")
    
# print("\nAddition is: ",num1+num2)
# print("Multiplication is: ",num1*num2)
# print("Division is: ",num1/num2)





print("Program to add, multiply and divide two integers and float numbers.")

ch = input("Enter 1 for Integer and 2 for Float: ")

if ch=='1':
    num1 = int(input("Enter First Float Number: "))
    num2 = int(input("Enter Second Float Number: "))  
    print("\nAddition is: ",num1+num2)
    print("Multiplication is: ",num1*num2)
    print("Division is: ",num1/num2)
    
elif ch=='2':
    num1 = float(input("Enter First Float Number: "))
    num2 = float(input("Enter Second Float Number: "))  
    print("\nAddition is: ",float(num1+num2))
    print("Multiplication is: ",float(num1*num2))
    print("Division is: ",float(num1/num2))
else:
    print("Invalid Choice: ")
    
