import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
input = input("Please press enter to see scatterplot of Petal length vs Petal width, by class")
#Create scatter plot, x = petal length, y = petal width

iris = pd.read_csv('iris2.csv')
x = iris['Petal length']
y = iris['Petal width']

plt.title("Iris data set: Petal length vs Petal width (all classes)")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

scatter = plt.scatter(x,y)
plt.show(scatter)

# nextinput = input("Please press enter to see boxplot of Sepal length vs Sepal width, by class")


bx = iris.boxplot(column = 'Sepal length', vert = False, by = 'Class')

plt.show(bx)


plt.subplot(2,2,1)
sns.boxplot(x="Class", y="Sepal length", data=iris)
plt.subplot(2,2,2)
sns.boxplot(x="Class", y="Sepal width", data=iris)
plt.subplot(2,2,3)
sns.boxplot(x="Class", y="Petal length", data=iris)
plt.subplot(2,2,4)
sns.boxplot(x="Class", y="Petal width", data=iris)

plt.show()