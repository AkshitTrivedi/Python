"""
 14. Write a Python program to remove duplicate values from Dictionary.
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
my_dict = { 'a' : 10, 'b' : 15, 'c' : 20, 'd' : 10, 'e' : 20}
  
print("The Original Dictionary is : \n" + str(my_dict))
  
temp = []
new_dict={}    #new_dict = dict()
for key, val in my_dict.items():
    if val not in temp:
        temp.append(val)
        new_dict[key] = val
  
print("The dictionary after removing duplicate values : \n" + str(new_dict))