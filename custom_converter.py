#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:48:33 2021

@author: chriswang
"""

import pandas as pd
import datetime as dt

def convert(label, df, dateformat, datelabel, timelabel, actlabel):
    
    file = open(label + " Formatted.csv", "w")
    file.write("DATE,TIME,ACTIVITY\n")
    
    # dropping rows until noon
    while(not (df['Time'][0].split(':')[0]+':'+df['Time'][0].split(':')[1] == '12:00')):
        df = df.drop([0])
        df = df.reset_index(drop=True)
    
    # writing data in output files and updating date format
    df = df[[datelabel, timelabel, actlabel]]
    for i in df.index:
        date = dt.datetime.strptime(df.iloc[i,0], dateformat)
        df.iloc[i,0] = date.strftime("%d/%m/%Y")
    print(df)
    df.to_csv(file, index=False, header=None)
    
    file.close()
    
    return pd.read_csv(label + " Formatted.csv")