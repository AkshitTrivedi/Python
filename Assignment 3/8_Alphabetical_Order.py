"""
 8. Write a program that will read a string and rewrite it in the alphabetical order.
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
# def sortString(str):                #done using sorted and join method
    # return ''.join(sorted(str))
      

sentence = input("Enter the string: ")
# print(sortString("Akki is my name"))

lst = list(sentence)            # convert string into list


for i in range(len(lst)-1):
    small_index = i
    for j in range(i+1, len(lst)):
        if lst[small_index].lower() > lst[j].lower():
            small_index = j
    lst[i], lst[small_index] = lst[small_index], lst[i]
    
alpha_str = "".join(lst)

print("\nString in Alphabetical Order: ",alpha_str)