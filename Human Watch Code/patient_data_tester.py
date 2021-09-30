#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:26:16 2021

@author: chriswang
"""

import pandas as pd
import os, sys

path = 'P36'
df = pd.read_csv(path+'/'+path+' Data Stitched 6-23-21.csv')
file = open(path+'/'+path+' Debugging.csv', 'w')

last = df['DATE'][0]
count = 1

print(len(df))

for i in range(1, len(df)):
    if (df['DATE'][i]==last):
        count = count + 1
    else:
        print(count)
        if (not (count == 1440 or count == 720)):
            df[i-1440:i].to_csv(file, index=False, header=None)
        count = 1
    last = df['DATE'][i]

file.close()