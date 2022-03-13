# -*- coding: utf-8 -*-
"""
This code is to create an ML model for pridiction of Real estate proce in Bangluru.
Created on Fri Mar  4 11:56:04 2022

@author: Aakash Tuteja
"""
# import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def convert_str_to_num(x):
    temp = x.split('-')
    if len(temp) == 2:
        return (float(temp[0])+float(temp[1]))/2
    try:
        return float(x)
    except:
        return np.nan


# Reading the raw csv file from Kaggle Datasets
df_raw = pd.read_csv('Bengaluru_House_Data.csv')


# Filtering the required columns
df1 = df_raw[['location', 'size', 'total_sqft', 'bath', 'price']]
df1 = df1.dropna()  # Deleting entire rows with null values as its % is <~2% (need to verify again)


# Removing extra keywords from size column and renaming it to Beds to verify
df1['Beds'] = df1['size'].apply(lambda x: int(x.split(' ')[0]))
del df1['size']  # Deleting size column as its useful data is fetched in new column


# Applying convert_str-to_num function to total_sqft column
df1['area'] = df1['total_sqft'].apply(convert_str_to_num)



