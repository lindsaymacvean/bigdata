#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:40:51 2019

@author: lindsaymacvean
"""

# matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

raw = pd.read_csv('./orders.csv')
raw.sort_values(by=['Number of Purchases'])

i = 0
maxValue = minValue = raw['Number of Purchases'].iloc[0]
total = 0

for index, row in raw.iterrows():
    i = i + 1
    if row['Number of Purchases'] > maxValue:
        maxValue = row['Number of Purchases']
    if row['Number of Purchases'] < minValue:
        minValue = row['Number of Purchases']
    total = total + row['Number of Purchases']
    
mean = total / i    

def median (count, data):
    col1 = data['Number of Purchases']
    middleIndex = count//2
    if count % 2 == 0:
        return (col1.iloc[middleIndex+1] + col1.iloc[middleIndex])/2
    else:
        return (col1.iloc[middleIndex+1] + col1.iloc[middleIndex])/2
        
print("max = " + str(maxValue))
print("min = " + str(minValue))
print("mean = " + str(mean))
print("median = " + str(median(i, raw)))

freqdiag = plt.subplot()
freqdiag.hist(raw['Number of Purchases'], bins=[50,59,69,79,89,99,110])
freqdiag.set_xlabel("number of purchases")
freqdiag.set_xticklabels(('0', '50', '59','69','79','89','99','109'))