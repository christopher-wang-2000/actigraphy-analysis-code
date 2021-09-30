#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:46:58 2021

@author: chriswang
"""

import pandas as pd
import os, sys

# input
df = pd.read_csv("P39/P39 Data Stitched 6-7-21.csv")
print(df)

# output
file = open("P39/P39 M10.csv", "w")
file.write("DATE,DAY,M10\n")

print(df[df["TIME"].str.contains("12:00:") == 1])
print(df.loc[0]["DATE"])

hourmean = 0
hourarray = [0]*24
m10 = 0

for i in range(len(df)):
    hourmean = hourmean + float(df.loc[i]["PIM"])
    if (i % 60 == 59):
        hourarray[(i % 1440)//60] = hourmean/60
        hourmean = 0
    if (i % 1440 == 1439):
        m10 = sum(sorted(hourarray)[-10:])/10
        file.write(df.loc[i]["DATE"]+","+str(i//1440+1)+","+str(m10)+"\n")
        print(m10)

file.close()