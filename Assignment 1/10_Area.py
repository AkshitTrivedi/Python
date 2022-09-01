# -*- coding: utf-8 -*-
"""
10.  Write a program to calculate the area of circle/rectangle/triangle. 
                    C indicate circle , 
                    R indicate rectangle,
                    T indicate triangle.
 use symbolic constant to define the value of pie.
 
 Name  : Akshit Trivedi           Roll No.: 40
 Class : MCA sem-1                Year    : 2021-22
"""

PI=3.14

print("\n Enter C for Circle")
print("\n Enter R for Ractangle")
print("\n Enter T for Triangle")

ch = input("Enter your Choice : ")

if(ch == 'C' or ch == 'c'):
    r = int(input("Enter Radius of Circle : "))
    area = PI * r * r;
    print("\nArea of Circle : ",area)
    
elif (ch == 'R' or ch == 'r'):
    w = int(input("Enter Width of rectangle : "))
    h = int(input("Enter Heigth of rectangle : "))
    area = w * h;
    print("\nArea of Rectangle : ",area)
    
elif(ch == 'T' or ch == 't'):
    b = int(input("Enter Base of triangle : "))
    h = int(input("Enter Heigth of triangle : "))
    area = (h * b)/2;
    print("\nArea of Triangle : ",area)
    
else:
    print("Invalid Choice!!! Please Try Again.")

    