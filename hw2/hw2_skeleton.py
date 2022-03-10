# -*- coding: utf-8 -*-
"""HW2_skeleton.py

# HW2 Matplotlib and Numpy (70 points)

##Electronic submission due 11:59pm, Thurs 2/24

To complete this homework, you need to download the data file named gradebook.txt, which contain the grades of 100 students in a class. The data file contains 100 rows, each of which represents a student, and 20 columns: the first 10 columns are quizzes, the next 7 columns are homeworks, and the last three columns are exams. 

Complete the python script to analyze the data and produce several statistics and three figures (see example figures on the next page).
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%% load data file

grades=pd.read_table('gradebook.txt',delimiter=' ', header=None).values

#%% 1. (5 points) Find out how many values in the array is negative or NaN, report the counts, and replace NaNs or negative values with 0.
print('Number of NaNs: ', )
print('Number of Zeros: ', )

#%% 2. (10 points) Generate a bar chart for the max of each column (20 bars).
plt.figure(1)
plt.xlabel('Column Index')
plt.ylabel('Max value')
plt.title('Fig 1')
plt.show()

#%% 3.	(10 points) Generate a bar chart for the mean of each HW (7 bars).

plt.figure(2)
plt.xlabel('HW Index')
plt.ylabel('Mean value')
plt.title('Fig 2')
plt.show()

#%% 4.	(10 points) Scatter plot the average of the two midterm exams exam against the final exam.
plt.figure(3)
plt.xlabel('Midterm Average')
plt.ylabel('Final exam')
plt.title('Fig 3')
plt.show()

#%% 5.	(10 points). Sort the final exam score (last column) to find the row index with the top 5 highest scores and report. Also report their grades for the three exams.

print('Row index for the top-5 final exam scores:', )

print('\nAll exam scores for the top-5 final exam scores:')

#%% 6.	(15 points) Compute a final weighted average score of each student: divide each column by the max of that column and then multiple by 100; and then compute a weighted average where each quiz counts 2%, each hw counts 5%, exam 1 and 2 each of which counts 10%, and the final exam counts 25%. Round the final score to the nearest integer. Report the following statistics for the final scores: max, min, median, mean, standard deviation.

print('Statistics  for final grade:')
print('\tmax: ')
print('\tmin: ', )
print('\tmedian: ', )
print('\tmean: ', )
print('\tstd: ', )

#%% 7.	(10 points) Count the number students whose final score is in the following range: < 60; >=60 and < 70, >=70 and < 80, >=80 and < 90, and >= 90, and plot the counts as a bar chart.

plt.figure(4)
categories = ('<60', '[60,70)', '[70,80)', '[80,90)', '>= 90')
plt.xticks(range(5), categories)
plt.ylabel('Number of students')
plt.xlabel('Final score')
plt.title('Fig 4')
plt.show()