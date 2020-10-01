# Author = Joseph Cameron
# preprocessGas-30.py
# Saves clean gas csv data, with boiler efficiency and COP values accounted for. 30 minute rounding.

# USAGE
# python preprocessGas-30.py gasData.csv

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

# Round the Datetimes to the nearest 30 minutes, in order to match electricity data
gas_data['Time'] = gas_data['Time'].dt.round('30min')

# Sum gas data within 30 minute buckets
gas_data = gas_data.reset_index().set_index('Time')
gas_data = gas_data.resample('30T').sum()

# ----------------------------------------------------------------------

# DELETE OUTLIERS

# First, remove readings that are negative, as this is clearly due to a sensor fault
gas_data = gas_data[gas_data["Sensor Value"] > 0]
# Secondly, remove readings that are unrealistically large, as this is also clearly due to sensor fault
# Assume that only points within the top percentile are too large
gas_data = gas_data[gas_data["Sensor Value"] < (gas_data["Sensor Value"].quantile(0.99) * 4)]

# ----------------------------------------------------------------------

# SAVE CSV

gas_data.to_csv('Clean-Gas-Data-30/' + sys.argv[1][10:15] + '_clean.csv', columns=['Sensor Value'], index=True)

# ----------------------------------------------------------------------

# SAVE/SHOW RESULTS

# Plot
#gas_data.plot(y='Sensor Value')

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
#plt.gcf().autofmt_xdate()

# Y axis label
#plt.ylabel("Watt Hours")

# Title
#plt.title(sys.argv[1][:4] + " Clean Gas Data")

#legendText = plt.legend()
#quantileVal = ideal_data["Energy"].quantile(0.99)
#legendText.get_texts()[0].set_text(quantileVal)

# Toggle comment if figure should be shown first
#plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[1] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
#plt.savefig('EnergyFigures/' + sys.argv[1][:4] + 'Energy_Figure.png', dpi=1000)
