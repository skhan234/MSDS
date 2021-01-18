# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:07:21 2021

@author: samee
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")

"Analysis for Age Variable"
mean_age = np.mean(df.Age)
max_age = np.max(df.Age)
min_age = np.min(df.Age)
print('Average Age: ' + str(round(mean_age,0)))
print('Maximum Age: ' + str(round(max_age,0)))
print('Minimum Age: ' + str(round(min_age,2)))

"Histogram for Passengers by Age"
plt.hist(df.Age, bins = 8, color = "blue", edgecolor="k")
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()

"Analysis for Survival Variable"
total_pass = len(df.Survived)
survived = len(df[df.Survived == 1])
not_survived = len(df[df.Survived == 0])
                   
print('Total Number of Passengers: ' + str(total_pass))
print('Total Passengers Survived: ' + str(survived))
print('Total Passengers Died: ' + str(not_survived))

"Graphing Survival Counts for Each Passenger Class"
first = df[df.Pclass == 1]
second = df[df.Pclass == 2]
third = df[df.Pclass == 3]

first_deaths = len(first[first.Survived==0])
second_deaths = len(second[second.Survived==0])
third_deaths = len(third[third.Survived==0])

first_survived = len(first[first.Survived==1])
second_survived = len(second[second.Survived==1])
third_survived = len(third[third.Survived==1])

ticket_class = ["First","Second","Third"]
class_deaths = np.array([first_deaths,second_deaths,third_deaths])
class_survived = np.array([first_survived,second_survived,third_survived])

ind = range(3)

plt.bar(ind,class_survived,label="Survived",color="green",bottom=class_deaths)
plt.bar(ind,class_deaths,label="Deaths",color="red")
plt.xticks(ind,ticket_class)
plt.ylabel("Number of Passengers")
plt.xlabel("Passenger Class")
plt.legend(loc="upper right")
plt.title("Titanic Passenger Survival/Death by Class")
plt.show


    