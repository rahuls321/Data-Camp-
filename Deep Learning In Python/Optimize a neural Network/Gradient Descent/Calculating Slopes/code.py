# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:05:40 2017

@author: hp
"""
"""Calculating Slopes"""

# Calculate the predictions: preds
preds = sum(weights * input_data)

# Calculate the error: error
error = preds - target

# Calculate the slope: slope
slope = input_data * error * 2

# Print the slope
print(slope)
