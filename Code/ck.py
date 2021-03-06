#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:20:08 2021

@author: chriswang
"""

# Calculates sleep/wake state according to the Cole-Kripke algorithm.
# Compared to Roenneberg, Cole-Kripke does not consolidate short periods
# of sleep into longer periods.

import pyActigraphy
import pandas as pd

def ck_calculator(label, df):

    raw = pyActigraphy.io.read_raw_awd(label+".AWD")
    
    file = open(label+' Cole-Kripke.csv', 'w')
    file.write('DATE,TIME,SLEEP\n')
    
    # Add mask over inactive periods (watch was dead or not worn)
    raw.create_inactivity_mask(duration='5h00min')
    raw.inactivity_length
    raw.mask_inactivity = True
    
    rest = raw.CK()    
    blankdf = pd.DataFrame()
    blankdf['DATE'] = df['DATE']
    blankdf['TIME'] = df['TIME']
    blankdf['WAKE'] = rest.values[0:len(blankdf['TIME'])]
    blankdf.to_csv(file, index=False, header=None)
    
    print("Cole-Kripke completed")
    file.close()
