# Author = Joseph Cameron
# monthlyOverallEnergyAverage.py
# Presents the average hourly energy demand within the timeframe of each month for all users (all .csv files in directory).

# USAGE
# Boxplot = python monthlyOverallEnergyAverage.py -b
# Line Graph = python monthlyOverallEnergyAverage.py -n

# --------------------------------------------------

# PARSE ARGUMENTS

import argparse

parser = argparse.ArgumentParser(description='Display an aggragated average over a day for each hour, minute or second.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-b', '--boxplot', action='store_true', help='Display a Boxplot.')
group.add_argument('-n', '--noboxplot', action='store_true', help='Do not display a Boxplot.')
args = parser.parse_args()

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

# --------------------------------------------------

# READ DATA

headers = ['Month','Hour','Sensor Value']

# Files within this directory
files = sorted(glob.glob('MonthlyAveEnergyCSV/*.csv'))

ideal_data = pd.DataFrame()

framelist = []

for f in files:
    df = pd.read_csv(f, names = headers, skiprows = 1)
    framelist.append(df)

ideal_data = pd.concat(framelist, ignore_index = True)

# --------------------------------------------------

# CREATE BOXPLOT
if args.boxplot:
    dailyData = ideal_data.boxplot(column='Sensor Value', by=['Month','Hour'], showmeans=True)
# CREATE MEAN LINE GRAPH
else:
    dailyData = ideal_data.groupby(["Month","Hour"]).mean().plot()

#-----------------------------------------------------

# SAVE/SHOW RESULTS

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the y-axis label
plt.ylabel("Watt Hours")

# Title
plt.title("Aggregated Average Hourly Energy Demand")

# Toggle comment if figure should be shown first
plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[3] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
#plt.savefig('EnergyFigures/' + sys.argv[3][-14:] + '_DailyAverage_Figure.png', dpi=1000)
