#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:24:17 2021

@author: chriswang
"""

import pandas as pd
import os, sys

#CHANGE LABEL TO CHANGE PATIENT
label = 'P41'
df_o = pd.read_csv(label+'/'+label+' Onsets+Offsets.csv')
df_ck = pd.read_csv(label+'/'+label+' Cole-Kripke.csv')
df_rb = pd.read_csv(label+'/'+label+' Roenneberg.csv')
file1 = open(label+'/'+label+' Awakening 5min Times.csv', 'w')
file1.write("DATE,DAY,ONSET,DURATION\n")
file2 = open(label+'/'+label+' Awakening 5min Summary.csv', 'w')
file2.write("DATE,DAY,NUMBER,TOTAL DURATION\n")

for i in range(len(df_ck)//1440):
    onset = 'N/A'
    duration = 0
    total = 0
    number = 0
    awakening = False
    beginning = True
    track = False
    #print(df_o['ONSET_TIME'][i])
    if (':' in str(df_o['ONSET_TIME'][i])):
        for j in range(1440):
            if (df_o['ONSET_TIME'][i] == df_rb['TIME'][1440*i+j]):
                track = True
            elif (df_o['OFFSET_TIME'][i] == df_rb['TIME'][1440*i+j]):
                print('Date: '+df_ck['DATE'][1440*i]+'; Number: '+str(number)+'; Total duration: '+str(total)+' min')
                file2.write(df_ck['DATE'][1440*i]+','+str(i+1)+','+str(number)+','+str(total)+'\n')
                continue
            if track:
                if ((df_ck['SLEEP'][1440*i+j] == 1) & beginning):
                    beginning = False
                if (not beginning):
                    if ((df_ck['SLEEP'][1440*i+j] == 0)):
                        duration = duration + 1
                        if (duration == 5):
                            awakening = True
                            onset = df_ck['TIME'][1440*i+j-4]
                    elif ((df_ck['SLEEP'][1440*i+j] == 1) & (not awakening)):
                        duration = 0
                    elif ((df_ck['SLEEP'][1440*i+j] == 1) & awakening):
                        #print(df_ck['DATE'][1440*i+j]+','+str(i+1)+','+onset+','+str(duration))
                        file1.write(df_ck['DATE'][1440*i+j]+','+str(i+1)+','+onset+','+str(duration)+'\n')
                        number = number + 1
                        total = total + duration
                        duration = 0
                        awakening = False
    else:
        print('Date: '+df_ck['DATE'][1440*i]+'; Number: N/A; Total duration: N/A')
        file2.write(df_ck['DATE'][1440*i]+','+str(i+1)+',N/A,N/A\n')
        
file1.close()
file2.close()