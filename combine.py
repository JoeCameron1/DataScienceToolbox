# Author = Joseph Cameron
# combine.py
# Combines clean gas and electricity data (as both have units of Wh) into an overall Energy CSV

# USAGE
# python combine.py gasData.csv electricityData.csv

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

# READ CLEAN GAS DATA

headers = ['Time', 'Sensor Value']
# Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
# Be careful with skiprows and skipfooter, maybe remove them
gas_data = pd.read_csv(sys.argv[1], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)
# Formatting dates
gas_data['Time'] = gas_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
# Set Index to be Datetime for correct join
gas_data = gas_data.reset_index().set_index('Datetime')

# ----------------------------------------------------------------------

# READ CLEAN ELECTRICITY DATA

# Get Electricity data
elec_data = pd.read_csv(sys.argv[2], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)
# Formatting dates
elec_data['Time'] = elec_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
# Set Index to be Datetime for correct join
elec_data = elec_data.reset_index().set_index('Datetime')

# ----------------------------------------------------------------------

# SUM GAS AND ELECTRICITY DATA ON CORRECT DATETIMES

# Join the gas and electricity data
ideal_data = elec_data.join(gas_data, lsuffix='_l', rsuffix='_r')

# Drop any rows that may contain null values
ideal_data = ideal_data.dropna(how='any')

# Create new Energy column, which is a sum of ASHP and electricity data
ideal_data['Energy'] = ideal_data['Sensor Value_l'] + ideal_data['Sensor Value_r']

# ----------------------------------------------------------------------

# DELETE OUTLIERS

# First, remove readings that are negative, as this is clearly due to a sensor fault
#ideal_data = ideal_data[ideal_data["Energy"] > 0]
# Secondly, remove readings that are unrealistically large, as this is also clearly due to sensor fault
# Assume that only points within the top percentile are too large
#ideal_data = ideal_data[ideal_data["Energy"] < (ideal_data["Energy"].quantile(0.99) * 4)]

# ----------------------------------------------------------------------

# SAVE ENERGY DEMAND CSV

# Save new CSV of energy data
ideal_data.to_csv('EnergyCSV/' + sys.argv[1][15:19] + '_Energy.csv', columns = ['Energy'], index=True)

# ----------------------------------------------------------------------

# SAVE/SHOW RESULTS

# Plot
ideal_data.plot(y='Energy')

# Variable used to create pickles
pickleVar = ideal_data

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Y axis label
plt.ylabel("Watt Hours")

# Title
plt.title(sys.argv[1][15:19] + " Clean Energy Data")

#legendText = plt.legend()
#quantileVal = ideal_data["Energy"].quantile(0.99)
#legendText.get_texts()[0].set_text(quantileVal)

# Toggle comment if figure should be shown first
plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
pickle.dump(pickleVar, file('EnergyPickles/' + sys.argv[1][15:19] + '_EnergyFigure.pickle','w'))

# Save Figure in the 'Figures' directory
#plt.savefig('EnergyFigures/' + sys.argv[1][15:19] + 'Energy_Figure.png', dpi=1000)