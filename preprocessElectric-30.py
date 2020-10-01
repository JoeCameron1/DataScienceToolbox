# Author = Joseph Cameron
# preprocessElectric-30.py
# Saves electric csv data in Watt Hours instead of Watts. 30 minute rounding.

# USAGE
# python preprocessElectric-30.py electricityData.csv

# --------------------------------------------------

# IMPORT STATEMENTS

import pandas as pd

from datetime import datetime

import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pickle

import sys

# ----------------------------------------------------------------------

# READ ELECTRICITY DATA

headers = ['Time', 'Sensor Value']

# Get Electricity data
elec_data = pd.read_csv(sys.argv[1], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)
# Formatting dates
elec_data['Time'] = elec_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

# Multiply all sensor values by (1/12) to get Wh instead of W
elec_data["Sensor Value"] = elec_data["Sensor Value"] * (1.0/12)

# Round the Datetimes to the nearest 30 minutes
elec_data['Time'] = elec_data['Time'].dt.round('30min')
# Sum gas data within 30 minute buckets
elec_data = elec_data.reset_index().set_index('Time')
elec_data = elec_data.resample('30T').sum()

# ----------------------------------------------------------------------

# DELETE OUTLIERS

# First, remove readings that are negative, as this is clearly due to a sensor fault
elec_data = elec_data[elec_data["Sensor Value"] > 0]
# Secondly, remove readings that are unrealistically large, as this is also clearly due to sensor fault
# Assume that only points within the top percentile are too large
elec_data = elec_data[elec_data["Sensor Value"] < (elec_data["Sensor Value"].quantile(0.99) * 4)]

# ----------------------------------------------------------------------

# SAVE CSV

elec_data.to_csv('Clean-Electric-Data-30/' + sys.argv[1][10:15] + '_clean.csv', columns = ['Sensor Value'], index=True)

# ----------------------------------------------------------------------

# SAVE/SHOW RESULTS

# Plot
#elec_data.plot(x='Datetime', y='Sensor Value')

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
#plt.gcf().autofmt_xdate()

# Y axis label
#plt.ylabel("Watt Hours")

# Title
#plt.title(sys.argv[1][:4] + " Clean Electric Data")

#legendText = plt.legend()
#quantileVal = ideal_data["Energy"].quantile(0.99)
#legendText.get_texts()[0].set_text(quantileVal)

# Toggle comment if figure should be shown first
#plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[1] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
#plt.savefig('EnergyFigures/' + sys.argv[1][:4] + 'Energy_Figure.png', dpi=1000)
