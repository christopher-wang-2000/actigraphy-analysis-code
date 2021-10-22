#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:58:39 2021

@author: chriswang
"""

import pandas as pd
import os, sys

def total_sleep_calculator(label):
    
    df = pd.read_csv(label+' Roenneberg.csv')
    df_o = pd.read_csv(label+' Onsets+Offsets.csv')
    file = open(label+' Sleep Bout Number (RB).csv', 'w')
    file.write("DATE,DAY,SLEEP BOUT NUMBER\n")

    for i in range(len(df)//1440):
        if (':' in str(df_o['ONSET_TIME'][i])):
            last = 1
            counter = 0
            for j in range(1440):
                if (df['SLEEP'][1440*i+j] == 1 and last == 0):
                    counter = counter + 1
                last = df['SLEEP'][1440*i+j]
            file.write(df['DATE'][1440*i]+','+str(i+1)+','+str(counter)+'\n')
        else:
            file.write(df['DATE'][1440*i]+','+str(i+1)+',N/A\n')
        
    file.close()
