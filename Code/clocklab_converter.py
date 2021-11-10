#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 6 14:39:35 2021

@author: chriswang
"""

import pandas as pd
import datetime as dt

def convert(label, df):
    
    file = open(label + " Formatted.csv", "w")
    file.write("DATE,TIME,ACTIVITY\n")
    
    startdate = df.iloc[1,1].split(" ")[-1]
    date = dt.datetime(int("20"+startdate.split("-")[2]), int(startdate.split("-")[1]), int(startdate.split("-")[0]))
    
    # keeps only the data rows in the dataframe
    df.columns = df.iloc[7]
    df = df.drop(df.index[range(8)])
    df = df.reset_index()
    
    # removes first column containing labels
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    
    for i in range(len(df.columns)-1):
        for j in range(1440):
            file.write(str(date.strftime("%d/%m/%Y")).split(" ")[0]+","+str(date).split(" ")[-1]+","+str(int(float(df.iloc[j,i+1])))+"\n")
            date = date + dt.timedelta(minutes=1)

    file.close()
    
    return pd.read_csv(label + " Formatted.csv")
