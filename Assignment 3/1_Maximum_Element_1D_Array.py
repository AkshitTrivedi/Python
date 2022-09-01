"""
 1. Write a program to find maximum element from 1-Dimensional array.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import array as arr

num1 = arr.array('i',[])

size = int(input("Enter the size of Array: "))

for i in range(size):
    item = int(input("Enter the item: "))
    num1.append(item)

print("Array Entered by you are: ", end="")

maximum = num1[i]

for i in range(size):
    print(num1[i], end=" ")
    if num1[i] > maximum:
         maximum = num1[i]

print("\nThe maximum of the array is: ", maximum)