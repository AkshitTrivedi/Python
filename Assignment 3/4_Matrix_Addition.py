"""
 4. Write a program to add two matrices.
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import numpy as np

rw = int(input("Enter the number of rows: "))
cl = int(input("Enter the number of column: "))
lst1 = []
lst2 = []

for i in range(0, rw*cl):
    item = int(input("Enter the item : "))
    lst1.append(item)

for i in range(0, rw*cl):
    item = int(input("Enter the item : "))
    lst2.append(item)

mat1 = np.array(lst1).reshape(rw,cl)
mat2 = np.array(lst2).reshape(rw,cl)
addition = np.empty([rw, cl], dtype=int)

for i in range(0, rw):
    for j in range(0, cl):
        addition[i][j] = mat1[i][j] + mat2[i][j]

print("\nMatrix Addition is: ")
for i in range(0, rw):
    for j in range(0, cl):
        print(mat1[i][j], end=" ")

    print("   ", end="")
    if i==0:
        print("+  ", end="")
    else:
     print("   ", end="")

    for j in range(0, cl):
        print(mat2[i][j], end=" ")

    print("   ", end="")

    if i==0:
        print("=  ", end="")
    else:
        print("   ", end="")

    for j in range(0, cl):
        print(addition[i][j], end=" ")
    
    print()