#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:14:27 2021

@author: chriswang
"""

import pandas as pd
import os, sys

labellist = ['P33', 'P34', 'P35', 'P36', 'P38', 'P39', 'P41']

for label in labellist:
    df = pd.read_csv(label+'/'+label+' Roenneberg.csv')
    file = open(label+'/'+label+' Onsets+Offsets.csv', 'w')
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
        if ((sum(df['SLEEP'][1440*i:1440*(i+1)])>0) & (sum(df['SLEEP'][1440*i:1440*(i+1)])<1440)):
            for j in range(1440):
                if (bout & (df['SLEEP'][1440*i+j]==1)):
                    boutlength = boutlength + 1
                elif ((not bout) & (df['SLEEP'][1440*i+j]==1)):
                    bout = True
                    boutlength = 1
                    tempondate = df['DATE'][1440*i+j]
                    tempontime = df['TIME'][1440*i+j]
                elif (bout & (df['SLEEP'][1440*i+j]==0)):
                    if (boutlength > maxbout):
                        maxbout = boutlength
                        ondate = tempondate
                        ontime = tempontime
                        offdate = df['DATE'][1440*i+j]
                        offtime = df['TIME'][1440*i+j]
                    bout = False
                    boutlength = 0
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