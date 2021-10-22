#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:14:27 2021

@author: chriswang
"""

# Identifies the sleep onsets and offsets based on the results of the
# Roenneberg sleep determination algorithm (MASDA)

import pandas as pd
import os, sys

def onset_offset_identifier(label):

    df = pd.read_csv(label+' Roenneberg.csv')
    file = open(label+' Onsets+Offsets.csv', 'w')
    file.write('DATE,DAY,ONSET_DATE,ONSET_TIME,ONSET_HOUR,OFFSET_DATE,OFFSET_TIME,OFFSET_HOUR\n')
    
    for i in range(len(df)//1440):
        maxbout = 0
        ondate = 'N/A'
        ontime = 'N/A'
        onhour = 'N/A'
        offdate = 'N/A'
        offtime = 'N/A'
        offhour = 'N/A'
        bout = False
        boutlength = 0
        tempondate = 'N/A'
        tempontime = 'N/A'
        temponhour = 'N/A'
        if ((sum(df['SLEEP'][1440*i:1440*(i+1)])>0) & (sum(df['SLEEP'][1440*i:1440*(i+1)])<1440)):
            for j in range(1440):
                if (bout & (df['SLEEP'][1440*i+j]==1)):
                    boutlength = boutlength + 1
                elif ((not bout) & (df['SLEEP'][1440*i+j]==1)):
                    bout = True
                    boutlength = 1
                    tempondate = df['DATE'][1440*i+j]
                    tempontime = df['TIME'][1440*i+j]
                    temponhour = (j/60.0 + 12) % 24
                elif (bout & (df['SLEEP'][1440*i+j]==0)):
                    if (boutlength > maxbout):
                        maxbout = boutlength
                        ondate = tempondate
                        ontime = tempontime
                        onhour = temponhour
                        offdate = df['DATE'][1440*i+j]
                        offtime = df['TIME'][1440*i+j]
                        offhour = (j/60.0 + 12) % 24
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
                        offtime = ((j/60.0 + 12) % 24) + (k/60.0)
        file.write(str(df.loc[i*1440]['DATE'])+','+str(i+1)+','+str(ondate)+','+str(ontime)+','+str(onhour)+','+str(offdate)+','+str(offtime)+','+str(offhour)+'\n')
                
    file.close()
