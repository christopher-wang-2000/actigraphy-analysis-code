#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:35:14 2021

@author: chriswang
"""

# Calculates the total amount of sleep each day based on the onsets and
# offsets determined from the results of the Roenneberg algorithm

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

def total_sleep_calculator(label, output):
    
    metric = "Total Sleep"
    
    df = pd.read_csv(label+' Roenneberg.csv')
    df_o = pd.read_csv(label+' Onsets+Offsets.csv')
    file = open(label+' '+metric+'.csv', 'w')
    file.write("DATE,DAY,TOTAL SLEEP\n")
    
    for i in range(len(df)//1440):
        if (':' in str(df_o['ONSET_TIME'][i])):
            counter = 0
            for j in range(1440):
                counter = counter + df['SLEEP'][1440*i+j]
            file.write(df['DATE'][1440*i]+','+str(i+1)+','+str(counter)+'\n')
        else:
            file.write(df['DATE'][1440*i]+','+str(i+1)+',N/A\n')
    
    file.close()
    
    # plot data with line of best fit
    df_ = pd.read_csv(label + " " + metric + ".csv")
    df_.dropna(inplace=True)
    x = df_["DAY"]
    y = df_["TOTAL SLEEP"]
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, y, "o")
    plt.plot(x, m*x + b)
    plt.xlabel("Day")
    plt.ylabel(metric + " (h)")
    plt.savefig(label + " Images/" + label + " " + metric + ".png")
    plt.clf()
    
    # calculate and output correlation
    r, p = scipy.stats.pearsonr(x, y)
    output.write(metric + "," + str(r) + "," + str(p) + "\n")
    
    print("Total sleep completed")
