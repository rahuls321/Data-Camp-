# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:05:59 2017

@author: hp
"""

""" Hierarchies of stocks """


# Import normalize
from sklearn.preprocessing import normalize

# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, method='complete') 

# Plot the dendrogram
dendrogram(mergings, labels = companies, leaf_rotation=90, leaf_font_size=6)
plt.show()
