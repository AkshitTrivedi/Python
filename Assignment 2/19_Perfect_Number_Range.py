"""
 19. Write a Python program to print all perfect numbers between given range
     using functions.
     
     [ perfect number is a positive integer that is equal to the sum of its
     positive divisor, excluding the number itself example 6 3+2+1= 6]
     
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""

start=int(input("Range Start From : "))
end=int(input("Range End : "))

def perfectnum():
    for num in range(start,end+1):
        sum=0
        
        for x in range(1,num):
            if num % x==0:              #if divisible by x then store in sum 
                sum =sum + x
                
        if (sum==num):
            print(num, end=' ')                
                       
print("Perfect numbers between %d and %d are:" %(start, end))
perfectnum()