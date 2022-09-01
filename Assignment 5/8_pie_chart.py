'''
8.  Write a program to display a pie chart for how many no of
    students take admission in different four courses at
    department. Courses like : MCA, PGDCSA, M.Sc.(AI&ML),
    M.Tech, etc.

Name  : Akshit Trivedi        Roll No.: 40
Class : MCA sem-1        Year    : 2021-22
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("addmision_student.csv")

x = df.Program.unique()
y= df.groupby(['Program'])['Id'].count()

plt.pie(y, labels = x)
plt.legend()
plt.show()