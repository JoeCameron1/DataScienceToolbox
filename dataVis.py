# Author = Joseph Cameron
# dataVis.py visualises data from the IDEAL dataset

# --------------------------------------------------
# IMPORT STATEMENTS

import pandas as pd

from datetime import datetime

import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pickle

import glob

# --------------------------------------------------

# Files within this directory
files = sorted(glob.glob('*.csv'))

# Processing all .csv files
for f in files:

    headers = ['Time', 'Sensor Value']
    # Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
    # Be careful with skiprows and skipfooter, maybe remove them
    ideal_data = pd.read_csv(f, parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)
    #print (ideal_data.columns)

    ideal_data['Time'] = ideal_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

    # Variable used to create pickles
    pickleVar = ideal_data
    
    # Axes
    x = ideal_data['Time']
    y = ideal_data['Sensor Value']

    # Plot
    plt.plot(x,y)

    # Properly format the x-labels
    plt.gcf().autofmt_xdate()

    # Toggle comment if figure should be shown first
    #plt.show()

    # Saving Pickle for future interactivity in the 'Pickles' directory
    pickle.dump(pickleVar, file('Pickles/' + f + '_Figure.pickle','w'))

    # Save Figure in the 'Figures' directory
    plt.savefig('Figures/' + f + '_Figure.jpg')