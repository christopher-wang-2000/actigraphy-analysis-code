#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:32:55 2021

@author: chriswang
"""

# Calculates IV: intradaily variability
# IV is a measure of minute-to-minute variability within a day.

def iv_calculator(label, df):

    file = open(label + " IV.csv", "w")
    file.write("DATE,DAY,IV\n")
    
    for i in range(len(df)//1440):
        daymean = sum(df["PIM"][i*1440:(i+1)*1440])/1440
        numerator = 0
        denominator = 0
        for j in range(1,1440):
            numerator = numerator + (df["PIM"][i*1440+j]-df["PIM"][i*1440+j-1])*(df["PIM"][i*1440+j]-df["PIM"][i*1440+j-1])
            denominator = denominator + (daymean - df["PIM"][i*1440+j])*(daymean - df["PIM"][i*1440+j])
        numerator = numerator * 1440
        denominator = denominator * 1439
        iv = 0
        if (denominator != 0):
            iv = numerator/denominator
        file.write(df.loc[i*1440]["DATE"]+","+str(i+1)+","+str(iv)+"\n")
    
    file.close()