#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:39:35 2021

@author: chriswang
"""

import pandas as pd
import os, sys
import datetime as dt

# REPLACE this with the correct path to where the stitched data files are stored
path = "Analysis (2021 Summer Chris Mice)/Data Stitched/"

fileList = os.listdir(path)
fileList = [i for i in fileList if "Data Stitched" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    df = pd.read_csv(path+name)
    startdate = df.iloc[1,0]
    print(startdate)
    
    identity = name.split("_")[0]
    print(identity)
    file = open(path+identity.split(' ')[0]+".AWD", "w")
    file.write(identity+'\n')
    
    # writing opening lines to Clocklab file
    startyear = startdate.split('-')[0]
    startmonth = startdate.split('-')[1]
    startday = startdate.split('-')[2]
    
    montharray = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    monthname = montharray[int(startmonth)-1]
    file.write(startday+"-"+monthname+"-"+startyear+"\n")
    print(startday+"-"+monthname+"-"+startyear)
    file.write(df.iloc[0,1].split(':')[0]+':'+df.iloc[0,1].split(':')[1]+'\n')
    print(df.iloc[0,1].split(':')[0]+':'+df.iloc[0,1].split(':')[1])
    file.write("4\n")
    file.write("1\n")
    file.write("1\n")
    file.write("1\n")
    
    for i in df['COUNTS']:
        file.write(str(i).split('.')[0]+'\n')
    
    file.close()