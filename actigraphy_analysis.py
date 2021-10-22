#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actigraphy Analysis Code
@author: Christopher Wang (christopher.wang@wustl.edu)
"""

import pandas as pd
import os, sys
import iv, m10, is_calc, awd, rb, ck, sri, onset_offset, total_sleep, midsleep, cpd

# prompts user for input: folder name containing files to be analyzed
path = input("Enter the name of the folder containing .csv files to be analyzed:")
if not path.endswith('/'):
    path = path + "/"
os.chdir("../"+path)
fileList = os.listdir()
fileList = [i for i in fileList if ".csv" in i]
fileList.sort()
print(fileList) # prints list of .csv files to be processed

for filename in fileList:
    
    # open the .csv as a dataframe
    df = pd.read_csv(filename)
    print("Analyzing " + filename + "...")
    
    # create the output folder and navigate into it
    label = filename[:-4]
    if not os.path.exists(label+"/"):
        os.makedirs(label+"/")
    os.chdir(label+"/")
    
    # run all analyses on each given file
    iv.iv_calculator(label, df)
    m10.m10_calculator(label, df)
    is_calc.is_calculator(label, df)
    awd.awd_converter(label, df)
    rb.rb_calculator(label, df)
    ck.ck_calculator(label, df)
    sri.sri_calculator(label)
    onset_offset.onset_offset_identifier(label)
    total_sleep.total_sleep_calculator(label)
    midsleep.midsleep_identifier(label)
    cpd.cpd_calculator(label)
    
    print(label + " analysis complete") 
    os.chdir("..")
