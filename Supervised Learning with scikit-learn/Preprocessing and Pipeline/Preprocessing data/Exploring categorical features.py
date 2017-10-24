# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:44:49 2017

@author: hp
"""



""" Exploring categorical features """



# Import pandas
import pandas as pd

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'Region', rot=60)

# Show the plot
plt.show()