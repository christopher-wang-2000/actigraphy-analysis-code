#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:14:27 2021

@author: chriswang
"""

# Identifies the midsleep of each sleep phase based on the onsets and offsets
# obtained from the results of the Roenneberg algorithm

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

def midsleep_identifier(label, output):
    
    metric = "Midsleep"

    df = pd.read_csv(label+' Onsets+Offsets.csv')
    file = open(label + " " + metric + ".csv", 'w')
    file.write('DATE,DAY,MIDSLEEP\n')
    
    for i in range(len(df)):
        onset = float(df.iloc[i]['ONSET_HOUR'])
        offset = float(df.iloc[i]['OFFSET_HOUR'])
        midsleep = (onset+offset)/2
        if offset < onset:
            midsleep = (onset-24+offset)/2
        
        file.write(df.iloc[i]['DATE']+','+str(i+1)+','+str(midsleep)+'\n')
        
    file.close()
    
    # plot data with line of best fit
    df_ = pd.read_csv(label + " " + metric + ".csv")
    df_.dropna(inplace=True)
    x = df_["DAY"]
    y = df_["MIDSLEEP"]
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, y, "o")
    plt.plot(x, m*x + b)
    plt.xlabel("Day")
    plt.ylabel(metric)
    plt.savefig(label + " Images/" + label + " " + metric + ".png")
    plt.clf()
    
    # calculate and output correlation
    r, p = scipy.stats.pearsonr(x, y)
    output.write(metric + "," + str(r) + "," + str(p) + "\n")
    
    print("Midsleep complete")
