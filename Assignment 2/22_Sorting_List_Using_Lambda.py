"""
 22. Write a Python program to sort a list of tuples using Lambda.
     Original list of tuple:-
     [('English',88),('Science',90),('Maths',97),('Socialsciences',82)]
     Resultant tuple:-
     [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
 
Name  : Akshit Trivedi           Roll No.: 40
Class : MCA sem-1                Year    : 2021-22     Practical Assignment-2
"""
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)

subject_marks.sort(key = lambda x: x[1])

print("\nSorting the List of Tuples:")
print(subject_marks)