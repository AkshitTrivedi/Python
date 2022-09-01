"""
5. Write a program that reads in two matrices and multiply them. Display the resultant matrix.
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import numpy as np

def matrix_mult(mat, rw):
    for i in range(rw):
        for j in range(rw):
            print(mat[i][j], end=" ")
        print()

cl = rw = int(input("Enter the number of rows and column: "))
    
lst1 = []
lst2 = []

for i in range(0, rw*cl):
    item = int(input("Enter Elements: "))
    lst1.append(item)

for i in range(0, rw*cl):
    item = int(input("Enter Elements: "))
    lst2.append(item)

mat1 = np.array(lst1).reshape(rw,cl)
mat2 = np.array(lst2).reshape(rw,cl)
mult = np.zeros([rw, cl], dtype=int)

for i in range(rw):
    for j in range(cl):
        for k in range(rw):
            mult[i][j] = mult[i][j] + (mat1[i][k] * mat2[k][j])
    
print("\nMatrix 1 is:")
matrix_mult(mat1, rw)
print("Matrix 2 is:")
matrix_mult(mat2, rw)
print("\nMatrix 1 * matrix 2:")
matrix_mult(mult, rw)