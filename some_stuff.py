NUMPY

#usually how you import numpy
#it's pretty much like matlab
import numpy as np

#array
np.array([1, 2, 3])
#you get array([3, 6, 9])

#makes a 3x3 matrix for A and B
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
A.shape
#you get (3, 3)

#numpy arrays are just like lists -- they're mutable
C = A
C[0, 0] = 1000
#here both A and C change. You're passing references not values.
#if you want to store temporary results you use copy/deep copy
C = A.copy()
#changing any element in C won't change A now

#slicing and taking the mean
np.mean(A[:,1])
#variance:
np.var(A)

////////////////////////////////////////////////////

MATPLOTLIB

#go on their website and fimd the kind of plot you want

import matplotlib.pyplot as plt

fig, axs = . . .
#axis is like a matrix with subplots or something like that?
#fig/figure is the whole thing

#when using Jupyter Notebook do %matplotlib inline and it'll show you
#the graphs and not the memory address.

////////////////////////////////////////////////////

PANDAS

#based on R where you have dataframes

import pandas as pd

d = {"A":[1, 2, 3, 4], "B":[5, 6, 7, 8]}
dataframe = pd.Dataframe(data=d)
#you get:
#   A   B
#--------
#0  1   5
#1  2   6
#2  3   7
#3  4   8

#you can do basic statistical analysis
#eg: count the number of entries above 6
#can use quickplot? if not familiar, use numpy
#"Unlike NumPy library which provides objects for multi-dimensional arrays,
#Pandas provides in-memory 2d table object called Dataframe."