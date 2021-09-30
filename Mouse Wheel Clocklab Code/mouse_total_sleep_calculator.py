#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:35:14 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
RBpath = "Analysis (2021 Summer Chris Mice)/Roenneberg/"
onoffpath = "Analysis (2021 Summer Chris Mice)/Sleep Onsets+Offsets/"
outputpath = "Analysis (2021 Summer Chris Mice)/Total Sleep/"

fileList = os.listdir(RBpath)
fileList = [i for i in fileList if "Roenneberg" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    identity = name.split(' ')[0]
    df = pd.read_csv(RBpath+identity+' Roenneberg.csv')
    df_o = pd.read_csv(onoffpath+identity+' Onsets+Offsets.csv')
    file = open(outputpath+identity+' Total Sleep Duration (RB).csv', 'w')
    file.write("DATE,DAY,TOTAL SLEEP\n")
    
    for i in range(len(df)//1440):
        if (':' in str(df_o['ONSET_TIME'][i])):
            counter = 0
            for j in range(1440):
                counter = counter + df['SLEEP'][1440*i+j]
            print('Date: '+df['DATE'][1440*i]+'; Duration: '+str(counter))
            file.write(df['DATE'][1440*i]+','+str(df['DAY'][1440*i])+','+str(counter)+'\n')
        else:
            print('Date: '+df['DATE'][1440*i]+'; Duration: N/A')
            file.write(df['DATE'][1440*i]+','+str(df['DAY'][1440*i])+',N/A\n')
        
    file.close()