"""
11. Write a program that search an item from array of string.
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import numpy as np

sentence = input("Enter the string: ")
find_str = input("Enter the item to find: ")
lst1 = sentence.split()

str_arr = np.array(lst1)

status = False
for i in range(len(str_arr)):
    if str_arr[i] == find_str:
        print("Word", find_str, "Found and it's Position is:",i+1)
        status = True
        break

if status==False:
    print("Word", find_str, "Not Found!!!")