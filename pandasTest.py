# Using Pandas to load contents of csv into data frame,
# #to filter, group and pivot data

# https://pandas.pydata.org
# https://pandas.pydata.org/pandas-docs/stable/10min.html


import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# loads the contents of iris2.csv ino a data frame called iris.
iris = pd.read_csv('iris2.csv')

# https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
headerlist= iris.columns.values.tolist()



print("The following are the top and bottom rows of the frame")
print(iris.head())
print()
print(iris.tail())
print()
# Select contents of the frame that meet specific criteria
print("the following is the first five records of subset of the dataset where class = 'Iris-versicolor:\n")
print(iris[iris['Class'] == 'Iris-versicolor'].head())

print("The following code will use SQL type features to group data by class and tell us facts of significance about each of the three classes of Iris")
print()
print("The following simply returns the number of records/observations by class")
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



# Next Pivot tables in pandas