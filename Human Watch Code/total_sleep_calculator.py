#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:35:14 2021

@author: chriswang
"""

import pandas as pd
import os, sys

#CHANGE LABEL TO CHANGE PATIENT
label = 'P35'
df = pd.read_csv(label+'/'+label+' Roenneberg.csv')
df_o = pd.read_csv(label+'/'+label+' Onsets+Offsets.csv')
file = open(label+'/'+label+' Total Sleep Duration (RB).csv', 'w')
file.write("DATE,DAY,TOTAL SLEEP\n")

for i in range(len(df)//1440):
    if (':' in str(df_o['ONSET_TIME'][i])):
        counter = 0
        for j in range(1440):
            counter = counter + df['SLEEP'][1440*i+j]
        print('Date: '+df['DATE'][1440*i]+'; Duration: '+str(counter))
        file.write(df['DATE'][1440*i]+','+str(i+1)+','+str(counter)+'\n')
    else:
        print('Date: '+df['DATE'][1440*i]+'; Duration: N/A')
        file.write(df['DATE'][1440*i]+','+str(i+1)+',N/A\n')
    
file.close()