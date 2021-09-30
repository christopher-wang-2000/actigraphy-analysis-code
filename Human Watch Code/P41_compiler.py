#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:48:33 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# REPLACE this with the correct path to where the data files are stored
path = "P41/"

fileList = os.listdir(path)
fileList = [i for i in fileList if "_2" in i]
fileList.sort()
print(fileList)

# output file: file1 = csv, file2 = Clocklab
# REPLACE these three lines with the correct names/labels
file1 = open(path+"P41 Data Stitched 6-25-21.csv", "w")
file2 = open(path+"P41 Data Clocklab 6-25-21.AWD", "w")
file2.write("P41\n")
file1.write("DATE,TIME,PIM,LIGHT\n")

# writing opening lines to Clocklab file
startdate2 = fileList[0].split("_")[1]
startyear2 = startdate2[0:4]
startmonth2 = startdate2[4:6]
startday2 = startdate2[6:8]
montharray = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
monthname = montharray[int(startmonth2)-1]
file2.write(startday2+"-"+monthname+"-"+startyear2+"\n")
file2.write("12:00\n")
file2.write("4\n")
file2.write("1\n")
file2.write("1\n")
file2.write("1\n")

for name in fileList:
    print(name)
    startdate = name.split("_")[1]
    enddate = name.split("_")[2].split(".")[0]
    startyear = startdate[0:4]
    startmonth = startdate[4:6]
    startday = startdate[6:8]
    if (startday[0] == "0"):
        startday = startday[1]
    startmonth2 = startmonth
    if (startmonth[0] == "0"):
        startmonth2 = startmonth[1]
    endyear = enddate[0:4]
    endmonth = enddate[4:6]
    endday = enddate[6:8]
    if (endday[0] == "0"):
        endday = endday[1]
    endmonth2 = endmonth
    if (endmonth[0] == "0"):
        endmonth2 = endmonth[1]
    sdslash = startday + "/" + startmonth + "/" + startyear
    sdslash2 = startday + "/" + startmonth2 + "/" + startyear
    edslash = endday + "/" + endmonth + "/" + endyear
    edslash2 = endday + "/" + endmonth2 + "/" + endyear
    
    data = pd.read_csv(path + name, delim_whitespace=True)
    header = ["DATE","TIME","PIM","LIGHT"]
    df = pd.DataFrame(data=data, columns=header)
    seconds = df["TIME"][0][6:8]
    print(sdslash)
    
    for i in range(1, len(df)):
        if (not ((int(df["TIME"][i].split(":")[1]) == int(df["TIME"][i-1].split(":")[1])+1)
            or (int(df["TIME"][i].split(":")[1]) == int(df["TIME"][i-1].split(":")[1])-59))):
            nextnum = int(df["TIME"][i-1].split(":")[1]) + 1
            if (int(df["TIME"][i-1].split(":")[1]) == 59):
                nextnum = 0
            if (nextnum < 10):
                nextnum = str('0'+str(nextnum))
            else:
                nextnum = str(nextnum)
            if (nextnum == '00'):
                newtime = df["TIME"][i-1].split(":")[0] + ':' + nextnum + ":" + df["TIME"][i].split(":")[2]
            else:
                newtime = df["TIME"][i].split(":")[0] + ':' + nextnum + ":" + df["TIME"][i].split(":")[2]
            df.loc[i-0.5] = df['DATE'][i-1], newtime, 0, 0
            df = df.sort_index().reset_index(drop=True)
    
    # check whether watch data extends all the way from 12:00 on start date to 11:59 on end date
    isStart = (((df["DATE"] == sdslash) | (df["DATE"] == sdslash2)) & (df["TIME"].str.count("12:00:"))).any()
    isEnd = (((df["DATE"] == edslash) | (df["DATE"] == edslash2)) & (df["TIME"].str.count("11:59:"))).any()
    
    startrow = 0
    if (isStart):
        startrow = df[((df["DATE"] == sdslash) | (df["DATE"] == sdslash2)) & (df["TIME"].str.count("12:00:"))].index[0]
        
    # if the data does not start at 12:00 on the start day, fill the space with 0s
    else:
        print(df["DATE"][0])
        if((df["DATE"][0] == sdslash) | (df["DATE"][0] == sdslash2)):
            print(df["TIME"][0])
            rows_list = []
            hour = int(df["TIME"][0].split(":")[0]) % 12
            minute = int(df["TIME"][0].split(":")[1])
            totalmin = 60*hour + minute
            mincounter = 0
            hcounter = 12
            for i in range(totalmin):
                minstring = str(mincounter)
                if (mincounter < 10):
                    minstring = "0" + minstring
                dict1 = {"DATE":sdslash, "TIME":(str(hcounter)+":"+minstring+":"+str(seconds)), "PIM":0, "LIGHT":0}
                rows_list.append(dict1)
                mincounter = mincounter+1
                if (mincounter == 60):
                    mincounter = 0
                    hcounter = hcounter+1
            blankdf = pd.DataFrame(rows_list)
            print(blankdf)
            blankdf.to_csv(file1, index=False, header=None)
            blankdf[["PIM","LIGHT"]].to_csv(file2, index=False, header=None)
        else:
            sys.exit("ERROR - START DAY IS INCORRECT")
    
    if(isEnd):
        endrow = df[((df["DATE"] == edslash) | (df["DATE"] == edslash2)) & (df["TIME"].str.count("11:59:"))].index[0]+1
    else:
        endrow = len(df)
    
    # write the data from the corresponding rows in the watch data into the output
    print(df[startrow:endrow])
    df[startrow:endrow].to_csv(file1, index=False, header=None)
    df[["PIM","LIGHT"]][startrow:endrow].to_csv(file2, index=False, header=None)
    
    # if the data does not extend all the way to 11:59 on the end date, fill the space with 0s
    if(not isEnd):
        rows_list = []
        hcounter = int(df["TIME"][len(df)-1].split(":")[0])
        mincounter = int(df["TIME"][len(df)-1].split(":")[1])
        day = int(df["DATE"][len(df)-1].split("/")[0])
        month = int(df["DATE"][len(df)-1].split("/")[1])
        year = int(df["DATE"][len(df)-1].split("/")[2])
        if (year < 2000):
            year = year+2000
        while(not((year==int(endyear))and(month==int(endmonth2))and(day==int(endday))and(hcounter==11)and(mincounter==59))):
            mincounter = mincounter+1
            if (mincounter == 60):
                mincounter = 0
                hcounter = hcounter+1
            if (hcounter == 24):
                hcounter = 0
                day = day+1
            if ((month == 2) and (((day > 28) and (year%4 != 0)) or (day > 29))):
                day = 1
                month = month+1
            elif ((day > 30) and ((month == 4) or (month == 6) or (month == 9) or (month == 11))):
                day = 1
                month = month+1
            elif (day > 31):
                day = 1
                month = month+1
            if (month == 13):
                month = 1
                year = year+1
            if (year > 2021):
                sys.exit("INFINITE LOOP - FILLING IN END")
            minstring = str(mincounter)
            if (mincounter < 10):
                minstring = "0" + minstring
            dict1 = {"DATE":(str(day)+"/"+str(month)+"/"+str(year)), "TIME":(str(hcounter)+":"+minstring+":"+str(seconds)), "PIM":0, "LIGHT":0}
            rows_list.append(dict1)
        blankdf = pd.DataFrame(rows_list)
        print(blankdf)
        blankdf.to_csv(file1, index=False, header=None)
        blankdf[["PIM","LIGHT"]].to_csv(file2, index=False, header=None)

file1.close()
file2.close()