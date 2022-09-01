def fact(no):
    if no<=1:
        return 1
    else:
        return (no * fact(no-1))
num=int(input("Enter any Number to find Factorial: "))
ans=fact(num)
print("Factorial of",num, "is:",ans)

