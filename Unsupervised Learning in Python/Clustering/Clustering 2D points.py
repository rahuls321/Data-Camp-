# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:20:21 2017

@author: hp
"""

""" Clustering 2D points """ 


# Import KMeans
from sklearn.cluster import KMeans

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters = 3)

# Fit model to points
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)

