'''4. Write a program count no of lines, word and character in a file.

Name  : Akshit Trivedi
Roll No.: 40
Class : MCA sem-1   
Practical Assignment 4

'''

try:
    with open("2_word_count.txt","r") as f:
        lines=0
        space=0
        char=0
        for line in f:
            lines += 1
            for c in line:
                char += 1
                if c == " " or c=="\n" :
                    space += 1
            
    print("Line Count:",lines)
    print("Word Count:",space+1)
    print("Character count:",char)

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred: ",e)


