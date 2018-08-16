# Author = Joseph Cameron
# displayEnergy.py
# Saves csv data and figures that show a user's energy demand curves from gas and electricity data

# USAGE
# python displayEnergy.py gasData.csv electricityData.csv

# --------------------------------------------------

# IMPORT STATEMENTS

import pandas as pd

from datetime import datetime

import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pickle

import sys

# ---------------------------------------------------------------------

# READ AND MODEL GAS DATA

headers = ['Time', 'Sensor Value']
# Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
# Be careful with skiprows and skipfooter, maybe remove them
gas_data = pd.read_csv(sys.argv[1], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

# Formatting dates
gas_data['Time'] = gas_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

def boilerFunc(x):
    return x * 0.9

def copFunc(x):
    return x / 2.1

# Apply Boiler Efficiency of 90% to obtain useful heat
gas_data['Sensor Value'] = gas_data['Sensor Value'].apply(boilerFunc)

# Apply COP to obtain the ASHP electricity needs to provide the same useful heat given by a boiler
gas_data['Sensor Value'] = gas_data['Sensor Value'].apply(copFunc)

# Round the Datetimes to the nearest 5 minutes, in order to match electricity data
gas_data['Time'] = gas_data['Time'].dt.round('5min')

# Get an average for any duplicate Datetime readings
gas_data = gas_data.reset_index().set_index('Time')
gas_data = gas_data.resample('5T').mean()

# ----------------------------------------------------------------------

# READ ELECTRICITY DATA

# Get Electricity data
elec_data = pd.read_csv(sys.argv[2], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)
# Formatting dates
elec_data['Time'] = elec_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
# Match gas data index
elec_data = elec_data.reset_index().set_index('Time')

# ----------------------------------------------------------------------

# SUM ASHP AND ELECTRICITY DATA ON CORRECT DATETIMES

# Join the gas and electricity data
ideal_data = elec_data.join(gas_data, lsuffix='_l', rsuffix='_r')

# Drop any rows that may contain null values
ideal_data = ideal_data.dropna(how='any')

# Create new Energy column, which is a sum of ASHP and electricity data
ideal_data['Energy'] = ideal_data['Sensor Value_l'] + ideal_data['Sensor Value_r']

# ----------------------------------------------------------------------

# DELETE OUTLIERS

# First, remove readings that are negative, as this is clearly due to a sensor fault
ideal_data = ideal_data[ideal_data["Energy"] > 0]
# Secondly, remove readings that are unrealistically large, as this is also clearly due to sensor fault
# Assume that only points within the top percentile are too large
ideal_data = ideal_data[ideal_data["Energy"] < (ideal_data["Energy"].quantile(0.99) * 3)]

# ----------------------------------------------------------------------

# SAVE ENERGY DEMAND CSV

# Save new CSV of energy data
ideal_data.to_csv('EnergyCSV/' + sys.argv[1][:4] + 'Energy.csv', columns = ['Datetime', 'Energy'], index=False)

# ----------------------------------------------------------------------

# SAVE/SHOW RESULTS

# Plot
ideal_data.plot(x='Datetime', y='Energy')

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Y axis label
plt.ylabel("Watt Hours")

# Title
plt.title(sys.argv[1][:4] + " Energy Data")

# Toggle comment if figure should be shown first
#plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[1] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
plt.savefig('EnergyFigures/' + sys.argv[1][:4] + 'Energy_Figure.png', dpi=1000)
