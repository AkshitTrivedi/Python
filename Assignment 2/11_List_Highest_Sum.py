"""
11). Write a Python program to find the list in a list of lists whose sum of
     elements is the highest.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
lst = [[10,20,30], [41,51,61], [50,60,70], [100,80,90]]
print("\nList is: ",lst)
print("\n\nList with Highest Sum of Elements is: ",max(lst, key=sum))