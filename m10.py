#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:38:32 2021

@author: chriswang
"""

# Calculates M10: a measure of amplitude.
# M10 is the mean hourly activity of the most active ten-hour period each day.

def m10_calculator(label, df):

    file = open(label + " M10.csv", "w")
    file.write("DATE,DAY,M10\n")
    
    hourmean = 0
    hourarray = [0]*24
    meanarray = [0]*24
    m10 = 0
    
    for i in range(len(df)):
        hourmean = hourmean + float(df.loc[i]["PIM"])
        if (i % 60 == 59):
            hourarray[(i % 1440)//60] = hourmean/60
            hourmean = 0
        if (i % 1440 == 1439):
            for j in range(24):
                if (j < 15):
                    meanarray[j] = sum(hourarray[j:j+10])/10
                else:
                    meanarray[j] = sum(hourarray[j:24])+sum(hourarray[0:j-14])
            m10 = max(meanarray)
            file.write(df.loc[i-1439]["DATE"]+","+str(i//1440+1)+","+str(m10)+"\n")
            hourarray = [0]*24
            meanarray = [0]*24
                
    file.close()
