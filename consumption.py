# Author = Joseph Cameron
# consumption.py
# Displays total energy consumption sum over a dataset's lifetime for every given hour during a day, given day, given week and given month.

# USAGE
# Hourly Line Graph = python dailyAverage.py -d data.csv
# Daily Line Graph = python dailyAverage.py -g data.csv
# Weekly Line Graph = python dailyAverage.py -w data.csv
# Monthly Line Graph = python dailyAverage.py -m data.csv

# --------------------------------------------------

# PARSE ARGUMENTS

import argparse

parser = argparse.ArgumentParser(description='Display total energy consumption sum over the dataset lifetime for every given hour during a day, given day, given week and given month.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--default', action='store_true', help='Display for every hour.')
group.add_argument('-g', '--giorno', action='store_true', help='Display for every day.')
group.add_argument('-w', '--week', action='store_true', help='Display for every week.')
group.add_argument('-m', '--month', action='store_true', help='Display for every month.')
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

headers = ['Time', 'Sensor Value']
# Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
# Be careful with skiprows and skipfooter, maybe remove them
ideal_data = pd.read_csv(sys.argv[2], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

# Formatting dates
ideal_data['Time'] = ideal_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

# Variable for x-axis label
xlabel = "Default x-axis label"

# CREATE LINE GRAPH
# Group by hour, day, week or month and plot the sum
# HOUR
if args.default:
    dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).sum().plot()
    xlabel = "hours during the day 0-23"
# DAY
elif args.giorno:
    dailyData = ideal_data.groupby([ideal_data["Time"].dt.year, ideal_data["Time"].dt.month, ideal_data["Time"].dt.day]).sum().plot()
    xlabel = "days"
# WEEK
elif args.week:
    dailyData = ideal_data.groupby(ideal_data["Time"].dt.week).sum().plot()
    xlabel = "weeks"
# MONTH
elif args.month:
    dailyData = ideal_data.groupby(ideal_data["Time"].dt.month).sum().plot()
    xlabel = "months"
# DEFAULT = HOUR
else:
    dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).sum().plot()
    xlabel = "hours during the day 0-23"

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Y-Axis Label
plt.ylabel("Watt Hours")

# X-Axis Label
plt.xlabel("Time (in " + xlabel + ")")

# Title of Plot
plt.title("Energy Consumption Sum")

# Toggle comment if figure should be shown first
plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[3] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
#plt.savefig('Figures/' + sys.argv[3] + '_Figure.jpg')
