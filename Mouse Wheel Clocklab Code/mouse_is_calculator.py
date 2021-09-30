#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:53:24 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
inputpath = "Analysis (2021 Summer Chris Mice)/Data Stitched/"
outputpath = "Analysis (2021 Summer Chris Mice)/IS/"

fileList = os.listdir(inputpath)
fileList = [i for i in fileList if "Data Stitched" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    identity = name.split(' ')[0]
    
    # input
    df = pd.read_csv(inputpath+name)
    file = open(outputpath+identity+' IS.csv', 'w')
    file.write("DATE,DAY,IS\n")
    
    #EDIT BIN SIZE (DAYS) HERE
    binsize = 4
    
    for i in range(len(df)//(1440*binsize)):
        weeksum = 0
        weekmean = sum(df["COUNTS"][i*1440*binsize:(i+1)*1440*binsize])/(24*binsize)
        numerator = 0
        denominator = 0
        hourarray = [0]*24
        for j in range(i*1440*binsize,(i+1)*1440*binsize):
            if (j % 60 == 0):
                hoursum = sum(df["COUNTS"][j:j+60])
                hourarray[(j//60)%24] = hourarray[(j//60)%24] + hoursum
                denominator = denominator + (hoursum-weekmean)*(hoursum-weekmean)
        hourmean = [x/binsize for x in hourarray]
        for j in range(len(hourarray)):
            numerator = numerator + (hourmean[j]-weekmean)*(hourmean[j]-weekmean)
        stability = 0
        if (denominator != 0):
            stability = (numerator*binsize)/denominator
        file.write(df.loc[i*1440*binsize]["DATE"]+","+str(binsize*i+1)+","+str(stability)+"\n")
        print(stability)
    
    file.close()