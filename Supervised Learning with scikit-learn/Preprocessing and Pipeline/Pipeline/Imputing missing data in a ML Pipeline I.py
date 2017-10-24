# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:08:45 2017

@author: hp
"""

""" Imputing missing data in a ML Pipeline I """


# Import the Imputer module
from sklearn.preprocessing import Imputer 
from sklearn.svm import SVC

# Setup the Imputation transformer: imp
imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp),
        ('SVM', clf)]