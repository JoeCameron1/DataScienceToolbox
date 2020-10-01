# Author = Joseph Cameron
# showTimeGaps.py
# Looks for time gaps in data collection, and produces a graph to show how many gaps of varying sizes occur within the dataset.

# USAGE
# python showTimeGaps.py gasData.csv

# --------------------------------------------------

# IMPORT STATEMENTS

import pandas as pd

from datetime import datetime

import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pickle

import sys

import glob

import numpy as np
from numpy import diff
from matplotlib.pyplot import cm

# ---------------------------------------------------------------------

# Files within this directory
files = sorted(glob.glob('*.csv'))

# Line colours
colors = iter(cm.rainbow(np.linspace(0,1,23)))

overallCounts = []

for f in files:

    # READ AND MODEL GAS DATA

    headers = ['Time', 'Energy']
    # Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
    # Be careful with skiprows and skipfooter, maybe remove them
    gas_data = pd.read_csv(f, parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

    # Formatting dates
    gas_data['Time'] = gas_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

    # ----------------------------------------------------------------------

    # DELETE OUTLIERS

    # First, remove readings that are negative, as this is clearly due to a sensor fault
    gas_data = gas_data[gas_data["Energy"] > 0]
    # Secondly, remove readings that are unrealistically large, as this is also clearly due to sensor fault
    # Assume that only points within the top percentile are too large
    gas_data = gas_data[gas_data["Energy"] < (gas_data["Energy"].quantile(0.99) * 4)]

    # ----------------------------------------------------------------------

    # SOLVE TIME GAPS

    gaps = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,120,180,240,300,360,420,480,540,600,1200,1800,2400,3000,3600,4200,4800,5400,6000,12000,18000,24000,30000,36000,48000,54000,60000]
    counts = []
    for x in gaps:
        gas_data['OVER 5 MINS'] = (gas_data['Time'].diff()).dt.seconds > x
        #val = None
        #count = 0
        #for index in range(len(gas_data["Time"])):
            #if gas_data.iloc[index]["OVER 5 MINS"] == True:
                #val = gas_data.iloc[index]["Time"] - gas_data.iloc[index-1]["Time"]
                #gas_data.iloc[index]["Energy"] = gas_data.iloc[index]["Energy"] / val
                #count = count + 1
        counts.append(sum(gas_data['OVER 5 MINS']))

    # ----------------------------------------------------------------------

    # SAVE ENERGY DEMAND CSV

    # Save new CSV of energy data
    #ideal_data.to_csv('EnergyCSV/' + sys.argv[1][:4] + 'Energy.csv', columns = ['Datetime', 'Energy'], index=False)

    # ----------------------------------------------------------------------

    # SAVE/SHOW RESULTS

    #x = gaps
    #y = counts
    #dy = diff(y)
    #x = x[:-1]
    #dy = np.absolute(dy)
    #plt.plot(x,dy,color=next(colors),label=f)
    overallCounts.append(counts)

x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,120,180,240,300,360,420,480,540,600,1200,1800,2400,3000,3600,4200,4800,5400,6000,12000,18000,24000,30000,36000,48000,54000,60000]
y = np.array(overallCounts)
y = y.mean(axis=0)
dy = diff(y)
x = x[:-1]
dy = np.absolute(dy)
plt.plot(x,dy)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Count')
plt.xlabel('Gaps (seconds)')
plt.title('Number of Time Gaps > Time Gap Value')
#plt.legend()
plt.grid()
plt.show()

# Plot
#gas_data.plot(x='Datetime', y='Energy')

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
#plt.gcf().autofmt_xdate()

# Y axis label
#plt.ylabel("Watt Hours")

# Title
#plt.title(sys.argv[1][:4] + " Energy Data")

# Toggle comment if figure should be shown first
#plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[1] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
#plt.savefig('EnergyFigures/' + sys.argv[1][:4] + 'Energy_Figure.png', dpi=1000)
