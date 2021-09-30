#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:53:46 2021

@author: chriswang
"""

import pandas as pd
import os, sys
import numpy as np

#CHANGE LABEL TO CHANGE PATIENT
label = 'P39'
df = pd.read_csv(label+'/'+label+' Midsleep Times.csv')
total = 0
count = 0
df = df.dropna()
file = open(label+'/'+label+' CPD.csv', 'w')
file.write("DAY,dREF,dDD,CPD\n")

for i in range(len(df)):
    if (not '#' in df['MIDSLEEP'][i]):
        print(str(df['MIDSLEEP'][i]))
        total = total + float(df['MIDSLEEP'][i])
        count = count + 1

mean = total/count
print(mean)

for i in range(1, len(df)):
    if ((not '#' in df['MIDSLEEP'][i]) & (not '#' in df['MIDSLEEP'][i-1])):
        x = (mean - float(df['MIDSLEEP'][i]))
        y = (float(df['MIDSLEEP'][i-1]) - float(df['MIDSLEEP'][i]))
        cpd = (x*x + y*y)**0.5
        print(str(i+1)+','+str(round(x,4))+','+str(round(y,4))+','+str(round(cpd,4)))
        file.write(str(i+1)+','+str(round(x,4))+','+str(round(y,4))+','+str(round(cpd,4))+'\n')
        
    else:
        print(str(i+1)+',N/A,N/A,N/A')
        file.write(str(i+1)+',N/A,N/A,N/A\n')

file.close()
        