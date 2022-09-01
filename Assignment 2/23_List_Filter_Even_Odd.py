"""
 23. Write a Python program to filter a list of integers using Lambda
     Original list of numbers:-
     [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)

print("\nEven numbers from list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)

print("\nOdd numbers from list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)