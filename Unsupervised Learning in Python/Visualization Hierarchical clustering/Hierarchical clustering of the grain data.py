# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:57:10 2017

@author: hp
"""


""" Hierarchical clustering of the grain data """


# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Calculate the linkage: mergings
mergings = linkage(samples, method='complete')

# Plot the dendrogram, using varieties as labels
dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()
