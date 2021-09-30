#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:39:35 2021

@author: chriswang
"""

import pandas as pd
import os, sys
import datetime as dt

# REPLACE this with the correct path to where the data files are stored
inputpath = "Analysis (2021 Summer Chris Mice)/Clocklab Graph Data/"
outputpath = "Analysis (2021 Summer Chris Mice)/Data Stitched/"

fileList = os.listdir(inputpath)
fileList = [i for i in fileList if "Graph Data" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    df = pd.read_csv(inputpath+name, header=None)
    startdate = df.iloc[1,1].split(" ")[-1]
    print(startdate)
    
    date = dt.datetime(int("20"+startdate.split("-")[2]), int(startdate.split("-")[1]), int(startdate.split("-")[0]))
    
    df.columns = df.iloc[7]
    print(df)
    df = df.drop(df.index[range(8)])
    df = df.reset_index()
    
    #removes first and last days of data
    df.drop(columns=df.columns[2], axis=1, inplace=True)
    df.drop(columns=df.columns[-1], axis=1, inplace=True)
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    print(df)
    
    identity = name.split("_")[0]
    print(identity)
    file = open(outputpath+identity+" Data Stitched.csv", "w")
    file.write("DATE,TIME,DAY,MINUTE,COUNTS\n")
    
    for i in range(len(df.columns)-1):
        day = df.columns[i+1]
        print(day)
        for j in range(1440):
            file.write(str(date).split(" ")[0]+","+str(date).split(" ")[-1]+","+str(day)+","+str(df.iloc[j,0])+","+str(df.iloc[j,i+1])+"\n")
            date = date + dt.timedelta(minutes=1)

    file.close()