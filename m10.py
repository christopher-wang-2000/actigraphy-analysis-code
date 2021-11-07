#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:38:32 2021

@author: chriswang
"""

# Calculates M10: a measure of amplitude.
# M10 is the mean hourly activity of the most active ten-hour period each day.

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

def m10_calculator(label, df, output):

    metric = "M10"
    
    file = open(label + " " + metric + ".csv", "w")
    file.write("DATE,DAY,M10\n")
    
    hourmean = 0
    hourarray = [0]*24
    meanarray = [0]*15
    m10 = 0
    
    for i in range(len(df)):
        hourmean = hourmean + float(df.loc[i][df.columns[2]])
        if (i % 60 == 59):
            hourarray[(i % 1440)//60] = hourmean/60
            hourmean = 0
        if (i % 1440 == 1439):
            for j in range(15):
                meanarray[j] = sum(hourarray[j:j+10])/10
            m10 = max(meanarray)
            file.write(df.loc[i-1439][df.columns[0]]+","+str(i//1440+1)+","+str(m10)+"\n")
            hourarray = [0]*24
            meanarray = [0]*15
    
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
    
    print("M10 completed")