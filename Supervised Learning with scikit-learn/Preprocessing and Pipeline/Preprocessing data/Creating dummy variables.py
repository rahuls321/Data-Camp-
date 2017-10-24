# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:50:22 2017

@author: hp
"""

""" CREATING DUMMY VARIABLES"""

# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = df_region.drop('Region_America', axis=1)

# Print the new columns of df_region
print(df_region.columns)
