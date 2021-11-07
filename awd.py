#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:37:06 2021

@author: chriswang
"""

def awd_converter(label, df):
    
    file = open(label + ".AWD", "w")
    
    file.write(label+"\n") # ID
    startdate = df.iloc[0][df.columns[0]]
    startday = startdate.split('/')[0]
    startmonth = startdate.split('/')[1]
    startyear = startdate.split('/')[2]
    montharray = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    monthname = montharray[int(startmonth)-1]
    file.write(startday+"-"+monthname+"-"+startyear+"\n") # start date
    file.write("12:00\n") # start time
    file.write("4\n") # determines interval
    file.write("1\n") # filler text for misc. information fields
    file.write("1\n")
    file.write("1\n")
    df[df.columns[2]].to_csv(file, index=False, header=None) # write activity data
    
    print("AWD conversion completed")
    file.close()
