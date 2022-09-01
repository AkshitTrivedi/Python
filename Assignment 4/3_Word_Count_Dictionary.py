'''3 Write a program store each word from file and count how many time a particular word is in the file.

Name  : Akshit Trivedi
Roll No.: 40
Class : MCA sem-1   
Practical Assignment 4

'''

try:
    namedict = dict()

    with open("2_word_count.txt", "r") as f:
        for fileline in f:
            words = fileline.split(" ")
            for w in words:
                w = w.rstrip("\n")
                if w in namedict:                              
                    namedict[w] = namedict[w] + 1    
                else:
                    namedict[w] = 1 

    for word, count in namedict.items():
            print(word, ":", count)

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred: ",e)



