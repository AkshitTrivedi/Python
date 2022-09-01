n1=int(input("Enter Number1: "))
n2=int(input("Enter Number2: "))

print("\n===Before Swapping===")
print("Number 1: ",n1,"\nNumber 2: ",n2)

n3=n2
n2=n1
n1=n3

print("\n===After Swapping===")
print("Number 1: ",n1,"\nNumber 2: ",n2)

n1=n1+n2
n2=n1-n2
n1=n1-n2

print("\n===After Swapping without 3rd Variable===")
print("Number 1: ",n1,"\nNumber 2: ",n2)

n1,n2=n2,n1

print("\n===After Swapping using 3rd Way===")
# print("Number 1: ",n1,"\nNumber 2: ",n2)
print(f"Value of a ==> {n1}\nValue of b ==> {n2}")