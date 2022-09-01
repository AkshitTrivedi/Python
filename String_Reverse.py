s1=input("Enter any String: ")
#s1=s1.split()[0] #To take input only first word
print("Your Entered String: "+s1)
#s2=s1[::-1] String Reverse using String Slicing

# String Reverse using for Loop
s2=""
for i in s1:
    s2=i+s2
#print(len(s1))
#print(len(s2))
#print(type(s1))
print("\nReversed String is: "+s2)

""" OUTPUT

Enter any String: !!!am ecnavdA ijragaS yaDhtriB yppaH
Your Entered String: !!!am ecnavdA ijragaS yaDhtriB yppaH

Reversed String is: Happy BirthDay Sagarji Advance ma!!!

 """

