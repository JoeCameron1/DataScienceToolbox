# Author = Joseph Cameron
# formatCSV.py removes strings from IDEAL .csv files

import pandas as pd

from datetime import datetime

import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pickle

import glob

files = sorted(glob.glob('*.csv'))

for f in files:
    print f