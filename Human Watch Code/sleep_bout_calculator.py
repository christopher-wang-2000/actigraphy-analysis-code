#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:58:39 2021

@author: chriswang
"""

import pandas as pd
import os, sys

#CHANGE LABEL TO CHANGE PATIENT
label = 'P41'
df = pd.read_csv(label+'/'+label+' Cole-Kripke.csv')
df_o = pd.read_csv(label+'/'+label+' Onsets+Offsets.csv')
file = open(label+'/'+label+' Sleep Bout Number (CK).csv', 'w')
file.write("DATE,DAY,SLEEP BOUT NUMBER\n")

for i in range(len(df)//1440):
    if (':' in str(df_o['ONSET_TIME'][i])):
        last = 1
        counter = 0
        for j in range(1440):
            if (df['SLEEP'][1440*i+j] == 1 and last == 0):
                counter = counter + 1
            last = df['SLEEP'][1440*i+j]
        print('Date: '+df['DATE'][1440*i]+'; Number: '+str(counter))
        file.write(df['DATE'][1440*i]+','+str(i+1)+','+str(counter)+'\n')
    else:
        print('Date: '+df['DATE'][1440*i]+'; Number: N/A')
        file.write(df['DATE'][1440*i]+','+str(i+1)+',N/A\n')
file.close()