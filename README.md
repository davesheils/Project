# Project

## Introduction and background

This project aims to use python to perform some analyses on the Fischer data set (also known as Andersons Iris data set). The dataset contains a set of 150 records under 5 headings/attributes - Petal Length , Petal Width , Sepal Length , Sepal width (all in cm) and Class (i.e the three species of Iris: Iris setosa, Iris virginica and Iris versicolor). This data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines (source: https://en.wikipedia.org/wiki/Iris_flower_data_set).

## Python Scripting

The purpose of this project was to use the python language to investigate the iris data set. The coding was broken down into three excercises:
The first was to use the numpy and statistics modules to perform some calculations on the numerical data colunms in the dataset. The code was used to find the following:
Mode (most common value)
Median
Average/Mean
Maximum and Minimum values
Standard deviation
www.numpy.org provides more information about this module. (Note that the statistics module was used to calculate the mode).

The next section of the exercise was an investigation of the pandas data analysis module. A particular focus of this part of the investigation was exploration of the concept of the data frame, i.e. the dataset as object with methods. For this section, a header was added to the iris dataset and saved as iris2.csv. The groupby and describe methods are used to output key stats about each class of iris, namely, the mean, standard deviation, the minimum, maximum and median (50%) values, and also the 25 and 75 percentile values. 
From there, the final section provides some examples of pythons data visualization features. The matplotlib.pyplot and seaborn modules are used.
The samples are a scatterplot of Petal Length vs Petal Width (undifferentiated by class) and a simple set of boxplots drawn from the Sepal length data. These plots are created using matplotlib.pyplot module. Finally, the seaborn module is used to create a set of boxplots for each numerical column, grouped by Class/Species. 
The three sections of the investigation were originally seperate scripts:
https://github.com/davesheils/Project/blob/master/numpyTest.py
https://github.com/davesheils/Project/blob/master/pandasTest.py
https://github.com/davesheils/Project/blob/master/plotTest.py
For the final submission, they have been consolidated into a single Project 2018 script:
https://github.com/davesheils/Project/blob/master/project2018.py

In order to run this script, the user should be able to run python 3.6. In addition, they should also have installed python via Anaconda or a similar package that contains the following modules:
numpy
statistics
matplotpy.pyplot
pandas
seaborn

## Findings

The following are the summary statistics found by the python script:
(1) Using Numpy:
The following sections list items of significance about each column containing numerical data to 2dp.

**Sepal length (cm)**
The most common value is 5.0.
The median is 5.8.
The average value is 5.84.
The maximum value is 7.9.
The minimum value is 4.3.
The standard deviation is 0.83.

**Sepal width (cm)**
The most common value is 3.0.
The median is 3.0.
The average value is 3.05.
The maximum value is 4.4.
The minimum value is 2.0.
The standard deviation is 0.43.

**Petal length (cm)**
The most common value is 1.5.
The median is 4.35.
The average value is 3.76.
The maximum value is 6.9.
The minimum value is 1.0.
The standard deviation is 1.76.

**Petal width (cm)**
The most common value is 0.2.
The median is 1.3.
The average value is 1.2.
The maximum value is 2.5.
The minimum value is 0.1.
The standard deviation is 0.76.

**(2) Using pandas:**
The first investigation simply returns the number of records/observations by class
Class
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50

The next section used the describe and groupby methods to return key statistics about each numberical column in the datasset, grouped by class of iris:
Sepal length
                 count   mean       std  min    25%  50%  75%  max
Class                                                             
Iris-setosa       50.0  5.006  0.352490  4.3  4.800  5.0  5.2  5.8
Iris-versicolor   50.0  5.936  0.516171  4.9  5.600  5.9  6.3  7.0
Iris-virginica    50.0  6.588  0.635880  4.9  6.225  6.5  6.9  7.9

Sepal width
                 count   mean       std  min    25%  50%    75%  max
Class                                                               
Iris-setosa       50.0  3.418  0.381024  2.3  3.125  3.4  3.675  4.4
Iris-versicolor   50.0  2.770  0.313798  2.0  2.525  2.8  3.000  3.4
Iris-virginica    50.0  2.974  0.322497  2.2  2.800  3.0  3.175  3.8

Petal length
                 count   mean       std  min  25%   50%    75%  max
Class                                                              
Iris-setosa       50.0  1.464  0.173511  1.0  1.4  1.50  1.575  1.9
Iris-versicolor   50.0  4.260  0.469911  3.0  4.0  4.35  4.600  5.1
Iris-virginica    50.0  5.552  0.551895  4.5  5.1  5.55  5.875  6.9

Petal width
                 count   mean       std  min  25%  50%  75%  max
Class                                                           
Iris-setosa       50.0  0.244  0.107210  0.1  0.2  0.2  0.3  0.6
Iris-versicolor   50.0  1.326  0.197753  1.0  1.2  1.3  1.5  1.8
Iris-virginica    50.0  2.026  0.274650  1.4  1.8  2.0  2.3  2.5
(3) Data Visualisation:

This is the most underdeveloped section of the project. The outputs of this section is three plots:
Simple scatterplot:
https://github.com/davesheils/Project/blob/master/irisScatterplot.png
Simple boxplot:
https://github.com/davesheils/Project/blob/master/irisSimpleBoxPlot.png
Four boxplots, one for each numerical column:
https://github.com/davesheils/Project/blob/master/iris4Boxplots1.png
Note, the code used for this last plot borrows significantly from the following: https://www.kaggle.com/vasanthreddy/data-visualisation-of-iris-dataset

## References
Background to iris data set:
https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson35-3
Source data downloaded from:
http://archive.ics.uci.edu/ml/datasets/Iris
Seaborn homepage:
https://seaborn.pydata.org/index.html
Pandas homepage:
https://pandas.pydata.org/
Matplotpy home page:
https://matplotlib.org/index.html
The following was useful in developing the clearscreen() function:
https://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
The following helped the use of the describe in conjuntion with groupby to output summary stats on each numerical column in the dataset:
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html
https://datascience.stackexchange.com/questions/22266/summary-statistics-by-category-using-python
The following was used as a model for the code to create the final set of boxplots:
https://www.kaggle.com/vasanthreddy/data-visualisation-of-iris-dataset




