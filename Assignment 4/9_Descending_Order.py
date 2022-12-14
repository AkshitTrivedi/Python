'''9. In program no 6 display information from file in descending order of percentage.

Name  : Akshit Trivedi
Roll No.: 40
Class : MCA sem-1   
Practical Assignment 4
'''


import pickle

class Student:
    def __init__(self):
        pass    

    def setDetails(self):
        self.roll = int(input("Enter Roll No: "))
        self.name = input("Enter your name: ")
        self.m1 = int(input("Enter Marks1: "))
        self.m2 = int(input("Enter Marks2: "))
        self.m3 = int(input("Enter Marks3: "))
        self.m4 = int(input("Enter Marks4: "))
        self.m5 = int(input("Enter Marks5: "))
        self.tot = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        self.per = (self.tot * 100)/500


    def display(self):
        print("\t\t\t\t\tMarksheet")
        print("Roll: ", self.roll)
        print("Name: ", self.name)
        print("m1: ", self.m1)
        print("m2: ", self.m2)
        print("m3: ", self.m3)
        print("m4: ", self.m4)
        print("m5: ", self.m5)
        print("Total Marks: ", self.tot)
        print("Percentage: ", self.per)

try:

    noofrec = int(input("Enter the number of records: "))
    with open("q6.dat", "wb") as f:
        for i in range(noofrec):
            print()
            s = Student()
            s.setDetails()
            pickle.dump(s,f)
    
    with open("q6.dat","rb") as f:
        for i in range(noofrec):
                obj=pickle.load(f)
                obj.display()
                print()

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred: ",e)


