# Author = Joseph Cameron
# total-robust-consumption.py
# Displays energy consumption for every hour, day, week and month.

# USAGE
# Hourly Line Graph = python total-robust-consumption.py -d Clean-Gas-Data/data.csv Clean-Electric-Data/data.csv
# Daily Line Graph = python total-robust-consumption.py -g Clean-Gas-Data/data.csv Clean-Electric-Data/data.csv
# Weekly Line Graph = python total-robust-consumption.py -w Clean-Gas-Data/data.csv Clean-Electric-Data/data.csv
# Monthly Line Graph = python total-robust-consumption.py -m Clean-Gas-Data/data.csv Clean-Electric-Data/data.csv

# --------------------------------------------------

# PARSE ARGUMENTS

import argparse

parser = argparse.ArgumentParser(description='Display a sum of energy consumption over every hour within a day, every day, every week or every month.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--default', action='store_true', help='Display for every hour.')
group.add_argument('-g', '--giorno', action='store_true', help='Display for every day.')
group.add_argument('-w', '--week', action='store_true', help='Display for every week.')
group.add_argument('-m', '--month', action='store_true', help='Display for every month.')
parser.add_argument('gasData', metavar='N', type=str, nargs='+', help='The .csv file containing gas data.')
parser.add_argument('electricData', metavar='N', type=str, nargs='+', help='The .csv file containing electric data.')
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

# READ ELECTRIC DATA

# Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
# Be careful with skiprows and skipfooter, maybe remove them
elec_data = pd.read_csv(sys.argv[3], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

# Formatting dates
elec_data['Time'] = elec_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

# Change index to Time for proper resampling
elec_data = elec_data.set_index("Time")

# --------------------------------------------------

# Variable for x-axis label
xlabel = "Default x-axis label"

# CREATE LINE GRAPH
# Resample by hour, day, week or month and plot the sum
# HOUR
if args.default:
    gasConsumption = gas_data.resample('H').sum().plot()
    electricConsumption = elec_data.resample('H').sum().plot()
    xlabel = "hours during the day 0-23"
# DAY
elif args.giorno:
    gasConsumption = gas_data.resample('D').sum()
    electricConsumption = elec_data.resample('D').sum()
    xlabel = "days"
# WEEK
elif args.week:
    gasConsumption = gas_data.resample('W').sum().plot()
    electricConsumption = elec_data.resample('W').sum().plot()
    xlabel = "weeks"
# MONTH
elif args.month:
    gasConsumption = gas_data.resample('M').sum().plot()
    electricConsumption = elec_data.resample('M').sum().plot()
    xlabel = "months"
# DEFAULT = HOUR
else:
    gasConsumption = gas_data.resample('H').sum().plot()
    electricConsumption = elec_data.resample('H').sum().plot()
    xlabel = "hours during the day 0-23"

# --------------------------------------------------

# SHOW PLOT

plt.plot(gasConsumption.index.get_values(), gasConsumption['Sensor Value'], label='Gas Consumption')
plt.plot(gasConsumption.index.get_values(), (gasConsumption['Sensor Value'] / 2.5), label='ASHP Consumption (COP = 2.5)')
plt.plot(electricConsumption.index.get_values(), electricConsumption['Sensor Value'], label='Electricity Consumption')

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Y-Axis Label
plt.ylabel("Watt Hours")

# X-Axis Label
plt.xlabel("Time (in " + xlabel + ")")

# Title of Plot
plt.title("Energy Consumption Sum")

# Legend of Plot
plt.legend()

# Show final plot
plt.show()
