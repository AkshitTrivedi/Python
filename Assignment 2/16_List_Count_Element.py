"""
 16. Write a program to determine frequency of number in a list of numbers.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
lst=[1,2,3,4,1,2,1,4,3,6,5,7,8,9,5,2,3,6,9,7,8,2,3,1,4,5,6,8]
print("\nList is:\n"+str(lst))
num=int(input("Enter the number : "))
print("The frequency of number ",num," is ",lst.count(num))