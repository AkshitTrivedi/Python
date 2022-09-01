"""
 7. Write a program that will read a text and cnt all occurrences of a particular word.
    
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-3
"""
sentence = input("Enter the String: ")
find_word = input("Enter the Word to find: ")

split_str = sentence.split(" ")
cnt = 0

for i in range(len(split_str)):
    if find_word == split_str[i].lower():
        cnt += 1

print("\nWord",find_word,"repeated:",cnt,"Times.")