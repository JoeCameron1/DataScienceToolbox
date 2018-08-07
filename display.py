# Author = Joseph Cameron
# display.py displays raw data from the IDEAL dataset

# USAGE
# python display.py data.csv

# --------------------------------------------------

# IMPORT STATEMENTS

import pandas as pd

from datetime import datetime

import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pickle

import sys

import glob

# --------------------------------------------------

# Files within this directory
files = sorted(glob.glob('*.csv'))

for f in files:

    headers = ['Time', 'Sensor Value']
    # Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
    # Be careful with skiprows and skipfooter, maybe remove them
    ideal_data = pd.read_csv(f, parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

    # Formatting dates
    ideal_data['Time'] = ideal_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

    # Plot
    ideal_data.plot(x='Time', y='Sensor Value', style='.')

    # Variable used to create pickles
    #pickleVar = ideal_data

    # Properly format the x-labels
    plt.gcf().autofmt_xdate()

    # Title
    plt.title(f + " Data")

    # Toggle comment if figure should be shown first
    #plt.show()

    # Saving Pickle for future interactivity in the 'Pickles' directory
    #pickle.dump(pickleVar, file('Pickles/' + f + '_Figure.pickle','w'))

    # Save Figure in the 'Figures' directory
    plt.savefig('Figures/' + f + '_Figure.png', dpi=500)