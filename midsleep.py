#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:14:27 2021

@author: chriswang
"""

# Identifies the midsleep of each sleep phase based on the onsets and offsets
# obtained from the results of the Roenneberg algorithm

import pandas as pd

def midsleep_identifier(label):

    df = pd.read_csv(label+' Onsets+Offsets.csv')
    file = open(label+' Midsleep.csv', 'w')
    file.write('DATE,DAY,MIDSLEEP\n')
    
    for i in range(len(df)):
        onset = float(df.iloc[i]['ONSET_HOUR'])
        offset = float(df.iloc[i]['OFFSET_HOUR'])
        midsleep = (onset+offset)/2
        if offset < onset:
            midsleep = (onset-24+offset)/2
        
        file.write(df.iloc[i]['DATE']+','+str(i+1)+','+str(midsleep)+'\n')
                
    file.close()
