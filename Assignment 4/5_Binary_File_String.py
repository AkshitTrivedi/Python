'''5. Write a program fetch the binary information from the file and convert it in to the string so 
that you can perform all the operation of string on that information.

Name  : Akshit Trivedi
Roll No.: 40
Class : MCA sem-1   
Practical Assignment 4

'''


try:
    with open("q5file.dat","rb") as f:
        str = f.read().decode()
        print(str)
except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred: ",e)
