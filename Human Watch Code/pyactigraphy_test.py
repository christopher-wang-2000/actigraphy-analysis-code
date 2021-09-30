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

#CHANGE LABEL TO CHANGE PATIENT

labellist = ['P33', 'P34', 'P35', 'P36', 'P38', 'P39']

for label in labellist:
    raw = pyActigraphy.io.read_raw_awd(label+'/'+label+' Data Clocklab PIM only 6-24.AWD')
    df = pd.read_csv(label+'/'+label+' Data Stitched 6-23-21.csv')
    
    #PLOTTING ACTIGRAPHY DATA
    plt.figure(1)
    plt.plot(raw.data)
    
    file = open(label+'/'+label+' Cole-Kripke.csv', 'w')
    file.write('DATE,TIME,SLEEP\n')
    
    #IGNORE
    #sstlog_csv = pyActigraphy.log.read_sst_log('Start Stop Times.csv')
    #print(sstlog_csv.log)
    #raw.apply_sst(verbose=True)
    #raw.frequency
    
    #ADD MASK AUTOMATICALLY
    raw.create_inactivity_mask(duration='5h00min')
    raw.inactivity_length
    
    if (label != 'P39'):
        #ADD MASK MANUALLY
        #raw.add_mask_periods(label+'/'+label+' Mask Log.csv')
        
        #PLOT MASK
        print(raw.mask)
        plt.figure(2)
        plt.plot(raw.mask)
        raw.mask_inactivity = True
    
    #ACTIVITY VARIABLE CALCULATION
    #output = raw.IVp(period='1D', binarize=False, verbose=True)
    #print(output)
    #plt.figure(3)
    #plt.plot(output)
    
    #SLEEP-WAKE DETERMINATION
    rest = raw.CK()
    plt.figure(4)
    plt.plot(rest)
    
    blankdf = pd.DataFrame()
    blankdf['DATE'] = df['DATE']
    blankdf['TIME'] = df['TIME']
    blankdf['WAKE'] = rest.values[0:len(blankdf['TIME'])]
    print(blankdf)
    blankdf.to_csv(file, index=False, header=None)
    file.close()