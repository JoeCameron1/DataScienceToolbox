# Author = Joseph Cameron
# dailyEnergySum.py presents the daily sum of energy usage

# USAGE
# python dailyEnergySum.py data.csv

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

# SUM DAILY ENERGY USE

ideal_data = ideal_data.groupby(by=ideal_data["Time"].dt.date).sum().plot()

# --------------------------------------------------

# PLOT

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Title
plt.title(sys.argv[1] + " Daily Sum")

# Toggle comment if figure should be shown first
plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[1] + '_Figure.pickle','w'))

# Save Figure in the 'EnergySumFigures' directory
#plt.savefig('EnergySumFigures/' + sys.argv[1] + '_Figure.png', dpi=1000)
