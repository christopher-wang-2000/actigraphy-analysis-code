#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:57:29 2021

@author: chriswang
"""

# Calculates SRI: sleep regularity index. SRI is a measure of regularity of
# sleep patterns across days. This calculation uses the sleep states
# determined by the Cole-Kripke algorithm.

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

def sri_calculator(label, output, binsize):
    
    metric = "SRI"
    
    df = pd.read_csv(label+' Cole-Kripke.csv')
    file = open(label+' '+metric+'.csv', 'w')
    file.write("DATE,DAY,SRI\n")
    
    for i in range(len(df)//(1440*binsize)):
        sriarray = [0]*binsize
        for j in range(binsize):
            if ((sum(df['SLEEP'][1440*binsize*i+1440*j:1440*binsize*i+1440*(j+1)])>100) & (sum(df['SLEEP'][1440*binsize*i+1440*(j+1):1440*binsize*i+1440*(j+2)])>100)):
                for k in range(1440):
                    if (df['SLEEP'][1440*binsize*i+1440*j+k] == df['SLEEP'][1440*binsize*i+1440*j+k+1440]):
                        sriarray[j] = sriarray[j] + 1/1440
        srisum = 0
        count = 0
        for e in sriarray:
            if (e > 0.2):
                srisum = srisum + e
                count = count + 1
        sriscaled = 'N/A'
        if (count > 2):
            srimean = srisum/count
            sriscaled = 200*(srimean-0.5)
        file.write(df.loc[i*1440*binsize]['DATE']+','+str(binsize*i+1)+','+str(sriscaled)+'\n')
    
    file.close()
    
    # plot data with line of best fit
    df_ = pd.read_csv(label + " " + metric + ".csv")
    df_.dropna(inplace=True)
    x = df_["DAY"]
    y = df_[metric]
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
    
    print("SRI completed")
