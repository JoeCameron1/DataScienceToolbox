# Author = Joseph Cameron
# dailyEnergyAverage.py
# Presents the average daily energy demand for a single user

# USAGE
# Hourly Boxplot = python dailyEnergyAverage.py -d -b data.csv
# Hourly Line Graph = python dailyEnergyAverage.py -d -n data.csv
# Boxplot for every minute = python dailyEnergyAverage.py -m -b data.csv
# Line Graph for every minute = python dailyEnergyAverage.py -m -n data.csv
# Boxplot for every second = python dailyEnergyAverage.py -s -b data.csv
# Line Graph for every second = python dailyEnergyAverage.py -s -n data.csv

# Note!!!!
# All other argument combinations will only save figures and not .csv data

# --------------------------------------------------

# PARSE ARGUMENTS

import argparse

parser = argparse.ArgumentParser(description='Display an aggragated average over a day for each hour, minute or second.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--default', action='store_true', help='Display for every hour.')
group.add_argument('-m', '--minute', action='store_true', help='Display for every minute.')
group.add_argument('-s', '--second', action='store_true', help='Display for every second.')
group2 = parser.add_mutually_exclusive_group()
group2.add_argument('-b', '--boxplot', action='store_true', help='Display a Boxplot.')
group2.add_argument('-n', '--noboxplot', action='store_true', help='Do not display a Boxplot.')
parser.add_argument('data', metavar='N', type=str, nargs='+', help='The .csv file containing data.')
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

# --------------------------------------------------

# READ DATA

headers = ['Time', 'Sensor Value']
# Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
# Be careful with skiprows and skipfooter, maybe remove them
ideal_data = pd.read_csv(sys.argv[3], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

# Formatting dates
ideal_data['Time'] = ideal_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

# --------------------------------------------------

# CREATE BOXPLOT
if args.boxplot:
    # Group by hour, minute or second and plot the mean values
    # HOUR
    if args.default:
        dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True)
        ideal_data = ideal_data.groupby(ideal_data["Time"].dt.hour).mean()
        # Save new CSV of energy data
        ideal_data.to_csv('DailyAveEnergyCSV/' + sys.argv[3][-14:] + 'DailyAverage.csv')
    # MINUTE
    elif args.minute:
        dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).boxplot(subplots=False, showmeans=True)
    # SECOND
    elif args.second:
        dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).boxplot(subplots=False, showmeans=True)
    # DEFAULT = HOUR
    else:
        dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True)
# CREATE MEAN LINE GRAPH
else:
    # Group by hour, minute or second and plot the mean values
    # HOUR
    if args.default:
        dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).mean().plot()
    # MINUTE
    elif args.minute:
        dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).mean().plot()
    # SECOND
    elif args.second:
        dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).mean().plot()
    # DEFAULT = HOUR
    else:
        dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).mean().plot()

#dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).mean().plot()
#dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).mean().plot()
#dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).mean().plot()

# --------------------------------------------------

# SAVE/SHOW RESULTS

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Y Label
plt.ylabel("Watt Hours")

# Title
plt.title(sys.argv[3][-14:] + " Average Hourly Energy Data")

# Toggle comment if figure should be shown first
#plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[3] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
plt.savefig('EnergyFigures/' + sys.argv[3][-14:] + '_DailyAverage_Figure.png', dpi=1000)
