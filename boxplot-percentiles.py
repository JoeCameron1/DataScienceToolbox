# Author = Joseph Cameron
# boxplot-percentiles.py
# Same as total-boxplot-consumption.py, except this prints the percentiles that are otherwise displayed in total-boxplot-consumption.py.

# USAGE
# Hourly Resampled Boxplot Percentiles = python boxplot-percentiles.py -d (Clean-Gas-Data/data.csv or Clean-Electric-Data/data.csv)
# Daily Resampled Boxplot Percentiles = python boxplot-percentiles.py -g (Clean-Gas-Data/data.csv or Clean-Electric-Data/data.csv)
# Weekly Resampled Boxplot Percentiles = python boxplot-percentiles.py -w (Clean-Gas-Data/data.csv or Clean-Electric-Data/data.csv)

# --------------------------------------------------

# PARSE ARGUMENTS

import argparse

parser = argparse.ArgumentParser(description='Display boxplot percentiles for energy consumption data.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--default', action='store_true', help='Resample for every hour.')
group.add_argument('-g', '--giorno', action='store_true', help='Resample for every day.')
group.add_argument('-w', '--week', action='store_true', help='Resample for every week.')
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

# DataFrame Headers
headers = ['Time', 'Sensor Value']

# --------------------------------------------------

# READ GAS DATA

# Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
# Be careful with skiprows and skipfooter, maybe remove them
gas_data = pd.read_csv(sys.argv[2], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

# Formatting dates
gas_data['Time'] = gas_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

# Change index to Time for proper resampling
gas_data = gas_data.set_index("Time")

# --------------------------------------------------

# GET PERCENTILES
# Resample by hourly sum, daily sum or weekly sum and produce the boxplot for every [year,month]
# HOUR
if args.default:
    gas_data = gas_data.resample('H').sum()
    percentile50 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.50)
    percentile75 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.75)
    percentile95 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.95)
# DAY
elif args.giorno:
    gas_data = gas_data.resample('D').sum()
    percentile50 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.50)
    percentile75 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.75)
    percentile95 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.95)
# WEEK
elif args.week:
    gas_data = gas_data.resample('W').sum()
    percentile50 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.50)
    percentile75 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.75)
    percentile95 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.95)
# DEFAULT = HOUR
else:
    gas_data = gas_data.resample('H').sum()
    percentile50 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.50)
    percentile75 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.75)
    percentile95 = gas_data.set_index(gas_data.index).groupby([gas_data.index.year, gas_data.index.month]).quantile(0.95)

# --------------------------------------------------

print percentile50
print percentile75
print percentile95

# Properly format the x-labels
#plt.gcf().autofmt_xdate()

# Y-Axis Label
#plt.ylabel("Watt Hours")

# X-Axis Label
#plt.xlabel("Time (in " + xlabel + ")")

# Title of Plot
#plt.title("Energy Consumption Boxplot")

# Legend of Plot
#plt.legend()

# Show final plot
#plt.show()
