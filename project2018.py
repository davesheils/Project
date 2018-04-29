# import modules 

import numpy as np
import statistics as stat
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# code to clear screen. Use clear if Unix, cls if windows (plese note: tested on Linux only)
def clearscreen():
    import platform
    import os
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

clearscreen()
print("Welcome to project 2018")
input("Press Enter to run the first section of code, i.e. using numpy to ouput stats about each column in the iris dataset.")


# Part 1 - Numpy test

# www.numpy.org

iris = np.genfromtxt('iris.csv', delimiter =',')

# create a list called header with the column names
header = ["Sepal length (cm)","Sepal width (cm)","Petal length (cm)","Petal width (cm)","Class"]

print("The following is the list of column headers in the iris dataset. Please note they are not in the original dataset")
for item in header:
    print(f"\t {item}")
print("This following code will test some of the features of numpy.")
print("The code will loop through the first four columns which contain numberic data and calculate the mode, mean, median, maximum and minimum values and standard deviation.")



print()
print("The following sections list items of significance about each column containing numerical data to 2dp.")     
print()


# Following loop will print the mean, median, mode and standard deviation of columns 0 - 3
for i in range (4):
    print(header[i])
    print(f"\t The most common value is {stat.mode(iris[:,i])}.")
    print(f"\t The median is {round(np.median(iris[:,i]),2)}.")
    print(f"\t The average value is {round(np.mean(iris[:,i]),2)}.")
    print(f"\t The maximum value is {round(np.max(iris[:,i]),2)}.")
    print(f"\t The minimum value is {round(np.min(iris[:,i]),2)}.")
    print(f"\t The standard deviation is {round(np.std(iris[:,i]),2)}.")
    print()

input("Press Enter to run the next section of code:")
clearscreen()

print("The next section uses the pandas data analysis modules to further investigate the iris dataset.")
print("Note that this code uses the iris2.csv file, the iris dataset with a header row added.")
print("The aim of this section is to explore the concept of a dataframe.")
print()

# Using Pandas to load contents of csv into data frame,

# https://pandas.pydata.org
# https://pandas.pydata.org/pandas-docs/stable/10min.html
# loads the contents of iris2.csv ino a data frame called iris.
iris = pd.read_csv('iris2.csv')

# https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
headerlist= iris.columns.values.tolist()



print("The following uses the head and tail methods to show the top and bottom rows of the frame")
print()
print(iris.head())
print()
print(iris.tail())
print()
# Select contents of the frame that meet specific criteria
print("The following is the first five records of subset of the dataset where class = 'Iris-versicolor:\n")
print(iris[iris['Class'] == 'Iris-versicolor'].head())
# https://datascience.stackexchange.com/questions/22266/summary-statistics-by-category-using-python
print("The following code will use the groupby method to group data by class and tell us facts of significance about each of the three classes of Iris")
print("The following simply returns the number of records/observations by class")
print()
print(iris.groupby('Class').size())
print()
print("The following returns the mean of each column grouped by class")
print()
print(iris.groupby('Class').agg({'Sepal length': np.mean, 'Sepal width': np.mean, 'Petal length': np.mean, 'Petal width':np.mean}))
print()
print("The following will use the 'describe' in conjunction with the groupby method to output summary statistics from each column, by class of iris")
print()

for i in range(0,4):
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html#
    print(headerlist[i])
    print(iris.groupby('Class')[headerlist[i]].describe())
    print()


input("Press Enter to run the next section of code, data visualization examples:")
clearscreen()
#Create scatter plot, x = petal length, y = petal width



# iris = pd.read_csv('iris2.csv')
x = iris['Petal length']
y = iris['Petal width']

plt.title("Iris data set: Petal length vs Petal width (all classes)")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

scatter = plt.scatter(x,y)
plt.show(scatter)

# 

bx = iris.boxplot(column = 'Sepal length', vert = False, by = 'Class')

plt.show(bx)

# The following closely follows the Seaborn example from 
# https://www.kaggle.com/vasanthreddy/data-visualisation-of-iris-dataset

plt.subplot(2,2,1)
sns.boxplot(x="Class", y="Sepal length", data=iris)
plt.subplot(2,2,2)
sns.boxplot(x="Class", y="Sepal width", data=iris)
plt.subplot(2,2,3)
sns.boxplot(x="Class", y="Petal length", data=iris)
plt.subplot(2,2,4)
sns.boxplot(x="Class", y="Petal width", data=iris)

plt.show()