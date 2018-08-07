# Author = Joseph Cameron
# displayASHP.py
# Save/Display the electricity needs of an Air Source Heat Pump to generate equivalent heat given by gas

# USAGE
# python displayASHP.py gasData.csv

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
ideal_data = pd.read_csv(sys.argv[1], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

# Formatting dates
ideal_data['Time'] = ideal_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

# --------------------------------------------------

# MODEL ASHP

def boilerFunc(x):
    return x * 0.9

def copFunc(x):
    return x / 2.1

# Apply Boiler Efficiency of 90% to obtain useful heat
ideal_data['Sensor Value'] = ideal_data['Sensor Value'].apply(boilerFunc)

# Apply COP to obtain the ASHP electricity needs to provide the same useful heat given by a boiler
ideal_data['Sensor Value'] = ideal_data['Sensor Value'].apply(copFunc)

# --------------------------------------------------

# SAVE/SHOW RESULTS

# Plot
ideal_data.plot(x='Time', y='Sensor Value')

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Y axis label
plt.ylabel("Watt Hours")

# Title
plt.title(sys.argv[1] + " Data")

# Toggle comment if figure should be shown first
#plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[1] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
plt.savefig('ASHPFigures/' + sys.argv[1] + '_Figure.png', dpi=1000)