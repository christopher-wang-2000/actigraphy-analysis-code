#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:20:08 2021

@author: chriswang
"""

import pyActigraphy
import matplotlib.pyplot as plt
import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
inputpath = "Analysis (2021 Summer Chris Mice)/Data Stitched/"
awdpath = "Analysis (2021 Summer Chris Mice)/AWD/"
outputpath = "Analysis (2021 Summer Chris Mice)/RA/"

fileList = os.listdir(inputpath)
fileList = [i for i in fileList if "Data Stitched" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    label = name.split(" ")[0]
    
    df = pd.read_csv(inputpath+name)
    print(df)
    
    raw = pyActigraphy.io.read_raw_awd(awdpath+label+'.AWD')
    
    #PLOTTING ACTIGRAPHY DATA
    #plt.figure(1)
    #plt.plot(raw.data)
    
    file = open(outputpath+label+' RA.csv', 'w')
    file.write('DATE,DAY,RA\n')
    
    #IGNORE
    #sstlog_csv = pyActigraphy.log.read_sst_log('Start Stop Times.csv')
    #print(sstlog_csv.log)
    #raw.apply_sst(verbose=True)
    #raw.frequency
    
    #ADD MASK AUTOMATICALLY
    raw.create_inactivity_mask(duration='24h00min')
    raw.inactivity_length
    
    #if (label != 'P39'):
        #ADD MASK MANUALLY
        #raw.add_mask_periods(label+'/'+label+' Mask Log.csv')
        
    #PLOT MASK
    #print(raw.mask)
    #plt.plot(raw.mask)
    #raw.mask_inactivity = True
    
    #ACTIVITY VARIABLE CALCULATION
    output = raw.RAp(period='1D', binarize=False, verbose=True)
    print(output)
    #plt.figure(3)
    #plt.plot(output)

    blankdf = pd.DataFrame()
    blankdf['DATE'] = df.iloc[::1440, :]['DATE']
    blankdf['DAY'] = df.iloc[::1440, :]['DAY']
    blankdf.drop(blankdf.tail(1).index,inplace=True)
    blankdf['RA'] = output
    print(blankdf)
    blankdf.to_csv(file, index=False, header=None)
    file.close()