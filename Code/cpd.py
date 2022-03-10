#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:53:46 2021

@author: chriswang
"""

import pandas as pd
import numpy as np
import math
import scipy
import matplotlib.pyplot as plt

def cpd_calculator(label, output):
    
    metric = "CPD"
    
    df = pd.read_csv(label+' Midsleep.csv')
    total = 0
    count = 0

    file = open(label+' '+metric+'.csv', 'w')
    file.write("DAY,dREF,dDD,CPD\n")

    for i in range(len(df)):
        if (not math.isnan(df['MIDSLEEP'][i])):
            total = total + float(df['MIDSLEEP'][i])
            count = count + 1

    mean = total/count

    for i in range(1, len(df)):
        if ((not math.isnan(df['MIDSLEEP'][i])) & (not math.isnan(df['MIDSLEEP'][i-1]))):
            x = (mean - float(df['MIDSLEEP'][i]))
            y = (float(df['MIDSLEEP'][i-1]) - float(df['MIDSLEEP'][i]))
            cpd = (x*x + y*y)**0.5
            file.write(str(i+1)+','+str(round(x,4))+','+str(round(y,4))+','+str(round(cpd,4))+'\n')
            
        else:
            file.write(str(i+1)+',N/A,N/A,N/A\n')
    
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
    
    print("CPD completed")