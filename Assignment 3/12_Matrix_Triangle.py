"""
 12. Write a program to read a matrix and determine the following :
    (1) wheather the given matrix is upper triangular or not
    (2) wheather the given matrix is lower triangular or not
    (3) wheather the given matrix is digonal matrix or not
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import numpy as np
def matrix_print(mat, rc):
    for i in range(rc):
        for j in range(rc):
            print(mat[i][j], end=" ")
        print()

def check_upper(mat, rc):
    for i in range(1, rc):
        for j in range(0, i):
            if mat[i][j] != 0:
                print("The Given matrix is not a upper triangular matrix")
                return
    print("The given matrix is upper triangular matrix")

def check_lower(mat, rc):
    for i in range(0, rc):
        for j in range(i+1, rc):
            if mat[i][j] != 0:
                print("The given matrix is not a lower triangular matrix")
                return
    print("The given matrix is lower triangular matrix")

def check_diagonal(mat, rc):
    for i in range(rc):
        for j in range(rc):
            if i!=j and mat[i][j] != 0:
                print("The given matrix is not a diagonal matrix")
                return
    print("The given matrix is diagonal matrix")

rc = int(input("Enter the number of rows and cols: "))
lst = []

for i in range(rc*rc):
    item = int(input("Enter Elements: "))
    lst.append(item)

mat1 = np.array(lst).reshape(rc, rc)

print("\nThe given matrix is: ")
matrix_print(mat1, rc)
check_upper(mat1, rc)
check_lower(mat1, rc)
check_diagonal(mat1, rc)