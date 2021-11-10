#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:32:55 2021

@author: chriswang
"""

# Calculates IV: intradaily variability
# IV is a measure of minute-to-minute variability within a day.

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

def iv_calculator(label, df, output):

    metric = "IV"
    
    file = open(label + " " + metric + ".csv", "w")
    file.write("DATE,DAY,IV\n")
    
    for i in range(len(df)//1440):
        daymean = sum(df[df.columns[2]][i*1440:(i+1)*1440])/1440
        numerator = 0
        denominator = 0
        for j in range(1,1440):
            numerator = numerator + (df[df.columns[2]][i*1440+j]-df[df.columns[2]][i*1440+j-1])*(df[df.columns[2]][i*1440+j]-df[df.columns[2]][i*1440+j-1])
            denominator = denominator + (daymean - df[df.columns[2]][i*1440+j])*(daymean - df[df.columns[2]][i*1440+j])
        numerator = numerator * 1440
        denominator = denominator * 1439
        iv = 0
        if (denominator != 0):
            iv = numerator/denominator
        file.write(df.loc[i*1440][df.columns[0]]+","+str(i+1)+","+str(iv)+"\n")
    
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
    
    print("IV completed")
