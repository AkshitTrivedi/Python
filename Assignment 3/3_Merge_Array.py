"""
3.  Given the two 1-D arrays A and B, which are sorted in ascending order. Write a program to merge
    them into a single sorted array C that contains every item from arrays A and B, in ascending order.
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
import array as arr

def print_array(sort_arr):
    size = len(sort_arr)
    for i in range(size):
        print(sort_arr[i], end=" ")

num1 = arr.array('i', [1, 2 , 3, 4, 5])
num2 = arr.array('i', [100, 200, 300 ,400 , 500])

merge = arr.array('i', [])

print("\nSorted Array 1: ", end="")
print_array(num1)
print("\nSorted Array 2: ", end="")
print_array(num2)

a=b=c=0   

while b != len(num1) and c != len(num2):    
    if num1[b] < num2[c]:
        merge.append(num1[b])
        b += 1
    else:
        merge.append(num2[c])
        c +=1
    a +=1

while b != len(num1):
    merge.append(num1[b])
    b += 1
    a += 1

while c != len(num2):
    merge.append(num2[c])
    c += 1
    a += 1

print("\nMerged Array: ", end="")
print_array(merge)