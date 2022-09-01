'''1. Write a program to create a file and input five person full name in file and read the information
from file. 

Name  : Akshit Trivedi
Roll No.: 40
Class : MCA sem-1   
Practical Assignment 4

'''


try:
    with open("1_person_name.txt", "w") as f:                        
        for i in range(5):
            name = input("Enter the name: ")
            f.write(name + "\n")                              

    print("Names are: ")
    with open("1_person_name.txt", "r") as file:        

        for fline in file:                                       
            print(fline.rstrip("\n"))
            print()

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred: ",e)

