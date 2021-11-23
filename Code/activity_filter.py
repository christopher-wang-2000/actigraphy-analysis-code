#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:23:40 2021

@author: chriswang
"""

# for IV, M10, IS: filters out days with activity below a threshold fraction of mean activity
def filter_days(df, threshold):
    
    daytotals = [] # tracks total activity for each day
    filtereddays = [] # tracks days that fall below the filter threshold
    count = 0
    
    # calculate number of counts per day
    for i in range(len(df)):
        count = count + float(df.loc[i][df.columns[2]])
        if (i % 1440 == 1439):
            daytotals.append(count)
            count = 0
    
    # determine which days fall below the threshold
    daymean = sum(daytotals)/len(daytotals) # get mean counts per day
    for i in range(len(daytotals)):
        if (daytotals[i] < threshold * daymean):
            filtereddays.append(i)
    
    return filtereddays