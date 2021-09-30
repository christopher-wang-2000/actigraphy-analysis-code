#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:14:27 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
inputpath = "Analysis (2021 Summer Chris Mice)/Roenneberg/"
outputpath = "Analysis (2021 Summer Chris Mice)/Sleep Onsets+Offsets/"

fileList = os.listdir(inputpath)
fileList = [i for i in fileList if "Roenneberg" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    identity = name.split(' ')[0]
    df = pd.read_csv(inputpath+name)
    file = open(outputpath+identity+' Onsets+Offsets.csv', 'w')
    file.write('DAY,ONSET_DATE,ONSET_TIME,OFFSET_DATE,OFFSET_TIME\n')
    
    for i in range(len(df)//1440):
        maxbout = 0
        ondate = 'N/A'
        ontime = 'N/A'
        offdate = 'N/A'
        offtime = 'N/A'
        bout = False
        boutlength = 0
        tempondate = 'N/A'
        tempontime = 'N/A'
        awakeninglength = 0
        awakeningthreshold = 30
        if ((sum(df['SLEEP'][1440*i:1440*(i+1)])>0) & (sum(df['SLEEP'][1440*i:1440*(i+1)])<1440)):
            for j in range(1440):
                if (bout & (df['SLEEP'][1440*i+j]==1)):
                    boutlength = boutlength + 1
                    awakeninglength = 0
                elif ((not bout) & (df['SLEEP'][1440*i+j]==1)):
                    bout = True
                    boutlength = 1
                    tempondate = df['DATE'][1440*i+j]
                    tempontime = df['TIME'][1440*i+j]
                elif (bout & (df['SLEEP'][1440*i+j]==0)):
                    if (awakeninglength <= awakeningthreshold):
                        awakeninglength = awakeninglength + 1
                    else:
                        if (boutlength > maxbout):
                            maxbout = boutlength
                            ondate = tempondate
                            ontime = tempontime
                            offdate = df['DATE'][1440*i+j-awakeninglength]
                            offtime = df['TIME'][1440*i+j-awakeninglength]
                        bout = False
                        boutlength = 0
                        awakeninglength = 0
                if ((j==1439) & bout):
                    k = 0
                    while ((1440*i+j+k<len(df)-1) & (df['SLEEP'][1440*i+j+k]==1)):
                        k = k+1
                        boutlength = boutlength + 1
                    if (boutlength > maxbout):
                        maxbout = boutlength
                        ondate = tempondate
                        ontime = tempontime
                        offdate = df['DATE'][1440*i+j+k]
                        offtime = df['TIME'][1440*i+j+k]
        print(str(i+1)+','+ondate+','+ontime+','+offdate+','+offtime)
        file.write(str(i+1)+','+ondate+','+ontime+','+offdate+','+offtime+'\n')
                
    file.close()