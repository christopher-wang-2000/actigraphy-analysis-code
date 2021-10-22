#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:35:14 2021

@author: chriswang
"""

# Calculates the total amount of sleep each day based on the onsets and
# offsets determined from the results of the Roenneberg algorithm

import pandas as pd
import os, sys

def total_sleep_calculator(label):

    df = pd.read_csv(label+' Roenneberg.csv')
    df_o = pd.read_csv(label+' Onsets+Offsets.csv')
    file = open(label+' Total Sleep (RB).csv', 'w')
    file.write("DATE,DAY,TOTAL SLEEP\n")
    
    for i in range(len(df)//1440):
        if (':' in str(df_o['ONSET_TIME'][i])):
            counter = 0
            for j in range(1440):
                counter = counter + df['SLEEP'][1440*i+j]
            file.write(df['DATE'][1440*i]+','+str(i+1)+','+str(counter)+'\n')
        else:
            file.write(df['DATE'][1440*i]+','+str(i+1)+',N/A\n')
        
    file.close()
