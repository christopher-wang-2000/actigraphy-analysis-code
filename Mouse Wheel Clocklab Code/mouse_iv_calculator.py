#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:32:55 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
inputpath = "Analysis (2021 Summer Chris Mice)/Data Stitched/"
outputpath = "Analysis (2021 Summer Chris Mice)/IV/"

fileList = os.listdir(inputpath)
fileList = [i for i in fileList if "Data Stitched" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    identity = name.split(" ")[0]
    print(identity)
    
    df = pd.read_csv(inputpath+name)
    print(df)
    
    # output
    file = open(outputpath+identity+" IV.csv", "w")
    file.write("DATE,DAY,IV\n")
    
    for i in range(len(df)//1440):
        daymean = sum(df["COUNTS"][i*1440:(i+1)*1440])/1440
        numerator = 0
        denominator = 0
        for j in range(1,1440):
            numerator = numerator + (df["COUNTS"][i*1440+j]-df["COUNTS"][i*1440+j-1])*(df["COUNTS"][i*1440+j]-df["COUNTS"][i*1440+j-1])
            denominator = denominator + (daymean - df["COUNTS"][i*1440+j])*(daymean - df["COUNTS"][i*1440+j])
        numerator = numerator * 1440
        denominator = denominator * 1439
        iv = 0
        if (denominator != 0):
            iv = numerator/denominator
        file.write(df.loc[i*1440]["DATE"]+","+str(df.loc[i*1440]["DAY"])+","+str(iv)+"\n")
        print(iv)
    
    file.close()