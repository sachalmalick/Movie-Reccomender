import numpy as np
import csv, string
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, neighbors
from scipy import spatial
import sklearn.datasets as datasets
from sklearn.linear_model import LinearRegression

def acc():
	wines = datasets.load_wine()
	X = wines.data
	Y = wines.target
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)
	clf = LinearRegression()
	clf.fit(X_train,y_train)
	accuracy = clf.score(X_test, y_test)
	return accuracy

l = [acc() for i in range(1000)]
print(sum(l) / 100)