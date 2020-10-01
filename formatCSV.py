# Author = Joseph Cameron
# formatCSV.py prints every IDEAL .csv file as a string
# Useful, as the strings can copy/pasted elsewhere easily, and later re-formatted.

# USAGE: python formatCSV.py

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
