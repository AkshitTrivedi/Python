"""
 15. Write a Python script to print a dictionary where the keys are numbers
     between 1 and 15 (both included) and the values are square of keys.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
square_dict=dict()
for x in range(1,16):
    square_dict[x]=x**2       #   **for power
print("\nSquare Dictionary is:\n",square_dict)