#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:53:24 2021

@author: chriswang
"""

# Calculates IS: interdaily stability
# IS is a measure of regularity of activity/sleep patterns across days.

def is_calculator(label, df):

    file = open(label + " IV.csv", "w")
    file.write("DATE,DAY,IS\n")
    
    for i in range(len(df)//(1440*7)):
        weekmean = sum(df["PIM"][i*1440*7:(i+1)*1440*7])/(24*7)
        numerator = 0
        denominator = 0
        hourarray = [0]*24
        for j in range(i*1440*7,(i+1)*1440*7):
            if (j % 60 == 0):
                hoursum = sum(df["PIM"][j:j+60])
                hourarray[(j//60)%24] = hourarray[(j//60)%24] + hoursum
                denominator = denominator + (hoursum-weekmean)*(hoursum-weekmean)
        hourmean = [x/7 for x in hourarray]
        for j in range(len(hourarray)):
            numerator = numerator + (hourmean[j]-weekmean)*(hourmean[j]-weekmean)
        stability = 0
        if (denominator != 0):
            stability = (numerator*7)/denominator
        file.write(df.loc[i*1440*7]["DATE"]+","+str(7*i+1)+","+str(stability)+"\n")
    
    file.close()