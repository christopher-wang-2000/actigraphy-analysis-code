#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:53:24 2021

@author: chriswang
"""

# Calculates IS: interdaily stability
# IS is a measure of regularity of activity/sleep patterns across days.

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

def is_calculator(label, df, output, binsize, filtereddays):

    metric = "IS"    

    file = open(label + " " + metric + ".csv", "w")
    file.write("DATE,DAY,IS\n")
    filtereddays = [x / binsize for x in filtereddays]
    
    for i in range(len(df)//(1440*binsize)):
        if (i not in filtereddays):
            weekmean = sum(df[df.columns[2]][i*1440*binsize:(i+1)*1440*binsize])/(24*binsize)
            numerator = 0
            denominator = 0
            hourarray = [0]*24
            for j in range(i*1440*binsize,(i+1)*1440*binsize):
                if (j % 60 == 0):
                    hoursum = sum(df[df.columns[2]][j:j+60])
                    hourarray[(j//60)%24] = hourarray[(j//60)%24] + hoursum
                    denominator = denominator + (hoursum-weekmean)*(hoursum-weekmean)
            hourmean = [x/binsize for x in hourarray]
            for j in range(len(hourarray)):
                numerator = numerator + (hourmean[j]-weekmean)*(hourmean[j]-weekmean)
            stability = 0
            if (denominator != 0):
                stability = (numerator*binsize)/denominator
            file.write(df.loc[i*1440*binsize][df.columns[0]]+","+str(binsize*i+1)+","+str(stability)+"\n")
        
    file.close()
    
    # plot data with line of best fit
    df_ = pd.read_csv(label + " " + metric + ".csv")
    df_.dropna(inplace=True)
    if (len(df_) >= 2):
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
    
    print("IS completed")