# Using Pandas to load contents of csv into data frame,
# #to filter, group and pivot data

# https://pandas.pydata.org
# https://pandas.pydata.org/pandas-docs/stable/10min.html


import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# loads the contents of iris2.csv ino a data frame called iris.
iris = pd.read_csv('iris2.csv')

print("The following are the top and bottom rows of the frame")
print(iris.head())
print()
print(iris.tail())
print()
# Select contents of the frame that meet specific criteria
print("the following is the subset of the dataset where class = 'Iris-versicolor:\n")
print(iris[iris['Class'] == 'Iris-versicolor'])


