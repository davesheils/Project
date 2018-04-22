# This script will test some of the features of numpy.
#



# mode, mean, median, max, min

import numpy as np
import statistics as stat # to ascertain mode

# pick one of the columns
# do mode, mean, median, max, min for all
#
iris = np.genfromtxt('iris.csv', delimiter =',') 
# loads contents of csv file as an array


# print the first and last row of data
print(iris[0])
print(iris[149])

# Note the 'nan' - not a number. All elements in a numpy array must be of the same data type.


# select first column from iris

col1 = iris[:,0]

print(col1)

# Print the mean, median, mode and standard deviation of column1

print(f"The most common value is {stat.mode(col1)}.")
print(f"The median is {np.median(col1)}.")
print(f"The average value is {np.mean(col1)}.")
print(f"The maximum value is {np.max(col1)}.")
print(f"The minimum value is {np.min(col1)}.")
print(f"The standard deviation is {np.std(col1)}.")
