"""
 17. Write a program to determine frequency of number in a list of numbers.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
def prime_interval(start, end):

    for num in range(start, end + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)

start=int(input("Range Start From : "))
end=int(input("Range End : "))

print("Prime numbers between", start, "and", end, "are:")
prime_interval(start,end)