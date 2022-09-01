"""
 6. Write a program to sort given string array in ascending order.
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import numpy as np

length = int(input("Enter the length of array: "))
lst = []

for i in range(length):
    item = input("Enter the string: ")
    lst.append(item)

names = np.array(lst)

print("\nBefore sorting: ", end=" ")

for i in range(length):
    print(names[i], end=" ")
    
for i in range(length-1):
    small_index = i
    for j in range(i, length):
        if names[small_index].lower() > names[j].lower():
            small_index = j
    names[i], names[small_index] = names[small_index], names[i]

print("\nAfter sorting: ", end=" ")

for i in range(length):
    print(names[i], end=" ")
