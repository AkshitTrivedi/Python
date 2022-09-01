start=int(input("Enter Start Number: "))
stop=int(input("Enter Stop Number: "))

# To print Odd Numbers
""" for i in range(start,stop+1):
    if(i%2==0):
        continue
    print(i) """

for n in range(start,stop+1):
    if n>1:
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            print(n)


num=int(input("Enter any Number: "))
count=0

if num>1:
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num,"is a Prime Number!!!")
    else:
        print(num,"is not a Prime Number!!!")
