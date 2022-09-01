"""
 13. Write a Python program to check if a given key already exists in a
     dictionary.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
dict = {'akshit': 1, 'python':2, 'java':3}

enter_key= input("Enter Key : ")


if enter_key in dict:
    print("The Key is Present and the Value is:",dict[enter_key])
else:
    print("The Key is not Present")