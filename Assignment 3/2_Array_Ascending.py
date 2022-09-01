"""
 2. Write a program to sort given array in ascending order.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import array as arr

def array_sort(a, size):
    for i in range(size):
        print(num1[i], end=" ")

num1 = arr.array('i',[])

size = int(input("Enter the size of array: "))

for i in range(size):
    item = int(input("Enter the item: "))
    num1.append(item)

print("Numbers Entered by you: ", end="")
array_sort(num1, size)

for i in range(size):                   # using selection sort
    min_index = i
    for j in range(i+1, size):
        if num1[min_index] > num1[j]:
            min_index = j
    
    num1[i], num1[min_index] = num1[min_index], num1[i]

print("\nThe sorted array is: ", end="")
array_sort(num1, size)