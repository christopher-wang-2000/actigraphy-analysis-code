#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:46:58 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
path = "Analysis (2021 Summer Chris Mice)/"

fileList = os.listdir(path+"Data Stitched")
fileList = [i for i in fileList if "Data Stitched" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    identity = name.split(" ")[0]
    print(identity)
    
    df = pd.read_csv(path+"Data Stitched/"+name)
    print(df)
    
    # output
    file = open(path+"Total Activity/"+identity+" Total Activity.csv", "w")
    file.write("DATE,DAY,COUNTS\n")
    
    for i in range(len(df)//1440):
        counts = sum(df["COUNTS"][i*1440:(i+1)*1440])
        file.write(df.loc[i*1440]["DATE"]+","+str(df.loc[i*1440]["DAY"])+","+str(counts)+"\n")
        print(counts)
    
    file.close()