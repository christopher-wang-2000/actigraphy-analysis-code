#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actigraphy Analysis Code
@author: Christopher Wang (christopher.wang@wustl.edu)
"""

import pandas as pd
import os, sys
import clocklab_converter, custom_converter, iv, m10, is_calc, awd, rb, ck, sri, onset_offset, total_sleep, midsleep, sleep_bout_calculator, cpd

default = False;
clocklab = False;
custom = False;

# prompts user for input: data file format
path = input("What format is your data in? Enter 1 for default format (DD/MM/YYYY Date, Time, Activity), 2 for Clocklab Graph Data, 3 for data with custom columns: ")
if (path == "1"):
    default = True
elif (path == "2"):
    clocklab = True
elif (path == "3"):
    custom = True
    datelabel = input("What is the name of the column containing the dates? ")
    timelabel = input("What is the name of the column containing the times of day? ")
    actlabel = input("What is the name of the column containing the activity data? ")
    path = input("What is the date format? Enter 1 for DD/MM/YYYY, 2 for DD/MM/YY, 3 for MM/DD/YYYY, 4 for MM/DD/YY, 5 for YYYY/MM/DD, or add 5 to any of these values if the separator is a hyphen instead of a slash: ")
    if (path == "1"):
        dateformat = "%d/%m/%Y"
    elif (path == "2"):
        dateformat = "%d/%m/%y"
    elif (path == "3"):
        dateformat = "%m/%d/%Y"
    elif (path == "4"):
        dateformat = "%m/%d/%y"
    elif (path == "5"):
        dateformat = "%Y/%m/%d"
    elif (path == "6"):
        dateformat = "%d-%m-%Y"
    elif (path == "7"):
        dateformat = "%d-%m-%y"
    elif (path == "8"):
        dateformat = "%m-%d-%Y"
    elif (path == "9"):
        dateformat = "%m-%d-%y"
    elif (path == "10"):
        dateformat = "%Y-%m-%d"
    else:
        print("Invalid input. Please restart the program.")
        sys.exit()
else:
    print("Invalid input. Please restart the program.")
    sys.exit()

# prompts user for input: diurnal or nocturnal
path = input("Are these data collected from diurnal (e.g. humans) or nocturnal (e.g. mice) animals? Enter D or N: ")
if (path == "D"):
    diurnal = True
elif (path == "N"):
    diurnal = False
else:
    print("Invalid input. Please restart the program.")
    sys.exit()

# prompts user for bin size for multi-day metrics
path = input("For multi-day metrics (IS, SRI), how many days (at least 2) should each bin contain? (Default: 7) ")
if (path.isdigit() and int(path) >= 2):
    binsize = int(path)
else:
    print("Unrecognized input. Using default bin size of 7 days.")
    binsize = 7

# prompts user for input: folder name containing files to be analyzed
path = input("Enter the name of the folder containing .csv files to be analyzed: ")
if not path.endswith('/'):
    path = path + "/"
os.chdir("../"+path)
fileList = os.listdir()
fileList = [i for i in fileList if ".csv" in i]
fileList.sort()
print(fileList) # prints list of .csv files to be processed

for filename in fileList:
    
    # open the .csv as a dataframe
    print("Analyzing " + filename + "...")
    if (clocklab):
        df = pd.read_csv(filename, header=None)
        label = filename[:-14]
    else:
        df = pd.read_csv(filename)
        label = filename[:-4]
    
    # create the output folder and navigate into it
    if not os.path.exists(label+"/"):
        os.makedirs(label+"/")
    os.chdir(label+"/")
    
    # create image folder
    if not os.path.exists(label+" Images/"):
        os.makedirs(label+" Images/")
    
    # converts file format if necessary
    if (clocklab):
        df = clocklab_converter.convert(label, df)
    if (custom):
        df = custom_converter.convert(label, df, dateformat, datelabel, timelabel, actlabel)
    
    df1 = df.copy()
    df2 = df.copy()
    
    if (diurnal):
        df1start = "0:00"
        df2start = "12:00"
    else:
        df1start = "12:00"
        df2start = "0:00"
    
    # drop rows until the data start at noon or midnight
    while(not (str(int(df1.iloc[0,1].split(':')[0]))+':'+df1.iloc[0,1].split(':')[1] == df1start)):
        df1 = df1.drop([0])
        df1 = df1.reset_index(drop=True)
        
    while(not (str(int(df2.iloc[0,1].split(':')[0]))+':'+df2.iloc[0,1].split(':')[1] == df2start)):
        df2 = df2.drop([0])
        df2 = df2.reset_index(drop=True)
        
    # open output file for correlations and p-values
    output = open(label + " Statistics.csv", "w")
    output.write("Metric,Pearson's Correlation (r),p-value\n")
    
    # run all analyses on each given file
    # IV, M10, and IS are calculated to include the entire window of the active period
    # sleep metrics are calculated to include the entire window of the sleep period
    iv.iv_calculator(label, df1, output)
    m10.m10_calculator(label, df1, output)
    is_calc.is_calculator(label, df1, output, binsize)
    awd.awd_converter(label, df2)
    rb.rb_calculator(label, df2)
    ck.ck_calculator(label, df2)
    sri.sri_calculator(label, output, binsize)
    onset_offset.onset_offset_identifier(label, output, diurnal)
    total_sleep.total_sleep_calculator(label, output)
    midsleep.midsleep_identifier(label, output)
    sleep_bout_calculator.sleep_bout_calculator(label, output)
    cpd.cpd_calculator(label, output)
    
    output.close()
    print(label + " analysis complete") 
    os.chdir("..")
