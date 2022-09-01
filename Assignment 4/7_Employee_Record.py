'''7 Write a program to insert employee record and read the data. Display the current position
in file while reading the data.

Name  : Akshit Trivedi
Roll No.: 40
Class : MCA sem-1   
Practical Assignment 4

'''

import pickle

class Employee:
    def __init__(self):
        pass  

    def setDetails(self):
        self.id = int(input("Enter id: "))
        self.name = input("Enter name: ")

    def showDetails(self):
        print("\n\t\t\t\t\tEmployee Details")
        print("Id: ", self.id)
        print("Name: ", self.name)
        

try:

    noofrec = int(input("Enter the number of records: "))
    with open("q6.dat", "wb") as f:
        for i in range(noofrec):
            print()
            s = Employee()
            s.setDetails()
            pickle.dump(s,f)
    
    with open("q6.dat","rb") as f:
        for i in range(noofrec):
                obj=pickle.load(f)
                obj.showDetails()
                print("Current position: ", f.tell())
                print()

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred: ",e)

