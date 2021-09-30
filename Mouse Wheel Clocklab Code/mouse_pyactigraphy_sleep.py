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
path = "Analysis (2021 Summer Chris Mice)/Data Stitched/"

fileList = os.listdir(path)
fileList = [i for i in fileList if "Data Stitched" in i]
fileList.sort()
print(fileList)

for name in fileList:
    
    label = name.split(" ")[0]
    
    df = pd.read_csv(path+name)
    print(df)
    
    raw = pyActigraphy.io.read_raw_awd(path+label+'.AWD')
    
    print('HELLO')
    
    #PLOTTING ACTIGRAPHY DATA
    #plt.figure(1)
    #plt.plot(raw.data)
    
    file = open(path+label+' Roenneberg.csv', 'w')
    file.write('DATE,TIME,DAY,MINUTE,RA\n')
    
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
    raw.mask_inactivity = True
    
    #SLEEP-WAKE DETERMINATION
    rest = raw.Roenneberg()
    plt.figure(4)
    plt.plot(rest)
    
    blankdf = pd.DataFrame()
    blankdf['DATE'] = df['DATE']
    blankdf['TIME'] = df['TIME']
    blankdf['DAY'] = df['DAY']
    blankdf['MINUTE'] = df['MINUTE']
    blankdf['WAKE'] = rest.values[0:len(blankdf['TIME'])]
    print(blankdf)
    blankdf.to_csv(file, index=False, header=None)
    file.close()