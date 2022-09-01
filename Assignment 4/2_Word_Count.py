'''2. Write a program to search a word in to the file. If word is found count number
of occurrence and print total no of occurrence for that word.

Name  : Akshit Trivedi
Roll No.: 40
Class : MCA sem-1   
Practical Assignment 4

'''


f=open("2_word_count.txt","r")  
word=input("Enter the word to match: ")
count=0
for file1 in f:
    w1=file1.split(" ") 
    for w in w1:        
        if(w.rstrip("\n")==word): 
            count+=1 

print("Total No of time", word,  "occurred in file:", count)