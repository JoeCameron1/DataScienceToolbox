# Author = Joseph Cameron
# seasonalAverage.py visualises data from the IDEAL dataset for every season

# USAGE
# python seasonalAverage.py [-d/-m/-s] [-b/-n] data.csv
# Hourly Boxplot = python seasonalAverage.py -d -b data.csv
# Hourly Line Graph = python seasonalAverage.py -d -n data.csv
# Boxplot for every minute = python seasonalAverage.py -m -b data.csv
# Line Graph for every minute = python seasonalAverage.py -m -n data.csv
# Boxplot for every second = python seasonalAverage.py -s -b data.csv
# Line Graph for every second = python seasonalAverage.py -s -n data.csv

# --------------------------------------------------

# PARSE ARGUMENTS

import argparse

parser = argparse.ArgumentParser(description='Display an aggragated average over a day for each hour, minute or second.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--default', action='store_true', help='Display for every hour.')
group.add_argument('-m', '--minute', action='store_true', help='Display for every minute.')
group.add_argument('-s', '--second', action='store_true', help='Display for every second.')
group2 = parser.add_mutually_exclusive_group()
group2.add_argument('-b', '--boxplot', action='store_true', help='Display a Boxplot.')
group2.add_argument('-n', '--noboxplot', action='store_true', help='Do not display a Boxplot.')
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

headers = ['Time', 'Sensor Value']
# Read .csv while getting rid of IDEAL data strings surrounding the data on the first and/or last rows
# Be careful with skiprows and skipfooter, maybe remove them
ideal_data = pd.read_csv(sys.argv[3], parse_dates = {"Datetime" : [0]}, names = headers, skiprows = 1, skipfooter = 1)

# Formatting dates
ideal_data['Time'] = ideal_data['Datetime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

# Set index
ideal_data = ideal_data.set_index(ideal_data['Time'])

# Create the figure
fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.set_ylabel('Temperature (0.1 Celsius)')
ax1.set_xlabel('Hours')
ax1.set_title('November - March')

ax2 = fig.add_subplot(222)
ax2.set_ylabel('Temperature (0.1 Celsius)')
ax2.set_xlabel('Hours')
ax2.set_title('April - May')

ax3 = fig.add_subplot(223)
ax3.set_ylabel('Temperature (0.1 Celsius)')
ax3.set_xlabel('Hours')
ax3.set_title('June - August')

ax4 = fig.add_subplot(224)
ax4.set_ylabel('Temperature (0.1 Celsius)')
ax4.set_xlabel('Hours')
ax4.set_title('September - October')

# CREATE BOXPLOT
if args.boxplot:
    # Group by hour, minute or second and plot the mean values
    # HOUR
    if args.default:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax4)
    # MINUTE
    elif args.minute:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).boxplot(subplots=False, showmeans=True, ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).boxplot(subplots=False, showmeans=True, ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).boxplot(subplots=False, showmeans=True, ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).boxplot(subplots=False, showmeans=True, ax=ax4)
    # SECOND
    elif args.second:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).boxplot(subplots=False, showmeans=True, ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).boxplot(subplots=False, showmeans=True, ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).boxplot(subplots=False, showmeans=True, ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).boxplot(subplots=False, showmeans=True, ax=ax4)
    # DEFAULT = HOUR
    else:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).boxplot(subplots=False, showmeans=True, ax=ax4)
# CREATE MEAN LINE GRAPH
else:
    # Group by hour, minute or second and plot the mean values
    # HOUR
    if args.default:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax4)
    # MINUTE
    elif args.minute:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).mean().plot(ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).mean().plot(ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).mean().plot(ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).mean().plot(ax=ax4)
    # SECOND
    elif args.second:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).mean().plot(ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).mean().plot(ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).mean().plot(ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).mean().plot(ax=ax4)
    # DEFAULT = HOUR
    else:
        ideal_data.loc['01/11/2016 00:00:00':'31/03/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax1)
        ideal_data.loc['01/04/2017 00:00:00':'31/05/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax2)
        ideal_data.loc['01/06/2017 00:00:00':'31/08/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax3)
        ideal_data.loc['01/09/2017 00:00:00':'31/10/2017 23:59:59'].groupby(ideal_data["Time"].dt.hour).mean().plot(ax=ax4)

#dailyData = ideal_data.groupby(ideal_data["Time"].dt.hour).mean().plot()
#dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute]).mean().plot()
#dailyData = ideal_data.groupby([ideal_data["Time"].dt.hour, ideal_data["Time"].dt.minute, ideal_data["Time"].dt.second]).mean().plot()

# Variable used to create pickles
#pickleVar = ideal_data

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Toggle comment if figure should be shown first
plt.show()

# Saving Pickle for future interactivity in the 'Pickles' directory
#pickle.dump(pickleVar, file('Pickles/' + sys.argv[3] + '_Figure.pickle','w'))

# Save Figure in the 'Figures' directory
#plt.savefig('Figures/' + sys.argv[3] + '_Figure.jpg')
