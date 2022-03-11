# -*- coding: utf-8 -*-
"""
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

df_raw = pd.read_csv('Bengaluru_House_Data.csv')

df1 = df_raw[['location', 'size', 'total_sqft', 'bath', 'price']]
df1 = df1.dropna()

df1['Beds'] = df1['size'].apply(lambda x: int(x.split(' ')[0]))

df2 = df1.copy()
df2['area'] = df2['total_sqft'].apply(convert_str_to_num)



