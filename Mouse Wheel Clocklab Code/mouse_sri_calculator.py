#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:57:29 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
CKpath = "Analysis (2021 Summer Chris Mice)/Cole-Kripke/"
outputpath = "Analysis (2021 Summer Chris Mice)/SRI/"

fileList = os.listdir(CKpath)
fileList = [i for i in fileList if "Cole-Kripke" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    identity = name.split(' ')[0]
    df = pd.read_csv(CKpath+identity+' Cole-Kripke.csv')
    file = open(outputpath+identity+' SRI.csv', 'w')
    file.write("DATE,DAY,SRI\n")
    
    #EDIT BIN SIZE (DAYS) HERE
    binsize = 4
    
    for i in range(len(df)//(1440*binsize)):
        sriarray = [0]*binsize
        for j in range(binsize):
            if ((sum(df['SLEEP'][1440*binsize*i+1440*j:1440*binsize*i+1440*(j+1)])>100) & (sum(df['SLEEP'][1440*binsize*i+1440*(j+1):1440*binsize*i+1440*(j+2)])>100)):
                for k in range(1440):
                    if (df['SLEEP'][1440*binsize*i+1440*j+k] == df['SLEEP'][1440*binsize*i+1440*j+k+1440]):
                        sriarray[j] = sriarray[j] + 1/1440
        srisum = 0
        count = 0
        for e in sriarray:
            if (e > 0.2):
                srisum = srisum + e
                count = count + 1
        sriscaled = 'N/A'
        if (count > 2):
            srimean = srisum/count
            sriscaled = 200*(srimean-0.5)
        file.write(df.loc[i*1440*binsize]['DATE']+','+str(binsize*i+1)+','+str(sriscaled)+'\n')
        print(sriscaled)
         
    file.close()