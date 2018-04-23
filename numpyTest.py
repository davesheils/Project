# This script will test some of the features of numpy.
# This is the second version, which loops through the first four columns which contain numberic data.

# mode, mean, median, max, min

import numpy as np
import statistics as stat # to ascertain mode

# pick one of the columns
# do mode, mean, median, max, min for all
#
iris = np.genfromtxt('iris.csv', delimiter =',') 
# loads contents of csv file as an array


# print the first and last row of data
# print(iris[0])
# print(iris[149])

# Note the 'nan' - not a number. All elements in a numpy array must be of the same data type.

# create a list called header with the column names

header = ["Sepal length (cm)","Sepal width (cm)","Petal length (cm)","Petal width (cm)","Class"]


# select first column from iris



# Following loop will print the mean, median, mode and standard deviation of columns 0 - 3
for i in range (3):
    print(header[i])
    print(f"\t The most common value is {stat.mode(iris[:,i])}.")
    print(f"\t The median is {np.median(iris[:,i])}.")
    print(f"\t The average value is {np.mean(iris[:,i])}.")
    print(f"\t The maximum value is {np.max(iris[:,i])}.")
    print(f"\t The minimum value is {np.min(iris[:,i])}.")
    print(f"\t The standard deviation is {np.std(iris[:,i])}.")
