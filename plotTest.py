import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#Create scatter plot, x = petal length, y = petal width

iris = pd.read_csv('iris2.csv')
x = iris['Petal length']
y = iris['Petal width']

plt.title("Iris data set: Petal length vs Petal width (all classes)")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

scatter = plt.scatter(x,y)
plt.show(scatter)

