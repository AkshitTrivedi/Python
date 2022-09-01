"""
 18. Write a Python program to print all Armstrong numbers between given
     range using functions.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
def armstrong_num(start, end):
    for num in range(start, end + 1):
        
        order = len(str(num))   
        sum = 0
        temp = num
        
        while temp > 0:
           digit = temp % 10
           sum += digit ** order
           temp //= 10
        
        if num == sum:
            print(num)

start=int(input("Enter Starting Range : "))
end=int(input("Enter Ending Range : "))

print("\nArmstrong numbers between", start, "and", end, "are:")
armstrong_num(start,end)