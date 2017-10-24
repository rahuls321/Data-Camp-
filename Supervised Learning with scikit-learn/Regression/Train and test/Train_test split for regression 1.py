# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:30:34 2017

@author: hp
"""
""" Train/test split for regression """
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train, y_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
mean = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mean)
print("Root Mean Squared Error: {}".format(rmse))