#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:49:44 2020

@author: jasonsteffener
"""
import pandas as pd
import glob
import os
import csv
import numpy as np
DirName = '/Users/jasonsteffener/Documents/GitHub/PowerMediationResults'
DirName = '/home/steffejr/Data'
fileName = "SubmissionList.csv"
df = pd.read_csv(os.path.join(DirName, fileName))

# Cycle over the list of result files and check to see if they are found

count = 0 
files = os.listdir(DirName)
for file in files:
    print(file)
    # Read the file    

    if file.endswith(".csv") and file.startswith('SimData'): 
         

        print(os.path.join(DirName, file))
        with open(os.path.join(DirName, file), newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            li = []
            for i in data: 
                li.append(i[0])

        # Find in the simulation list the values for this result
        flagNBoot = df['Nboot'] == int(float(li[0]))
        flagNSim = df['NSim'] == int(float(li[1]))
        flagN = df['N'] == int(float(li[2]))
        flagAtoB = df['AtoB'] == (float(li[3]))
        flagAtoC = df['AtoC'] == (float(li[4]))
        flagBtoC = df['AtoC'] == (float(li[5]))
        flagAtype = df['typeA'] == int(float(li[6]))
        mask = flagNBoot & flagNSim & flagN & flagAtoB & flagAtoC & flagAtype & flagBtoC
        # find the position of this value
        pos = np.flatnonzero(mask)
        df['Completed'][pos] = 1
        count += 1

df.to_csv(os.path.join(DirName, fileName))       
      
        
