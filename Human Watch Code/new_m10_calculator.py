#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:38:32 2021

@author: chriswang
"""

import pandas as pd
import os, sys

labellist = ['P33', 'P34', 'P35', 'P36', 'P38', 'P39', 'P41']

for label in labellist:
    df = pd.read_csv(label+'/'+label+' Data Stitched 6-23-21.csv')
    print(df)
    
    # output
    file = open(label+"/"+label+" M10 Fixed.csv", "w")
    file.write("DATE,DAY,M10\n")
    
    print(df[df["TIME"].str.contains("12:00:") == 1])
    print(df.loc[0]["DATE"])
    
    hourmean = 0
    hourarray = [0]*24
    meanarray = [0]*24
    m10 = 0
    
    for i in range(len(df)):
        hourmean = hourmean + float(df.loc[i]["PIM"])
        if (i % 60 == 59):
            hourarray[(i % 1440)//60] = hourmean/60
            hourmean = 0
        if (i % 1440 == 1439):
            for j in range(24):
                if (j < 15):
                    meanarray[j] = sum(hourarray[j:j+10])/10
                else:
                    meanarray[j] = sum(hourarray[j:24])+sum(hourarray[0:j-14])
            m10 = max(meanarray)
            print(df.loc[i-1439]["DATE"]+","+str(i//1440+1)+","+str(m10))
            file.write(df.loc[i-1439]["DATE"]+","+str(i//1440+1)+","+str(m10)+"\n")
            hourarray = [0]*24
            meanarray = [0]*24
                
    file.close()