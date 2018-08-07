# Author = Joseph Cameron
# showFig.py shows a figure of IDEAL data from a pickle file, given as a command-line argument

import matplotlib.pyplot as plt
import pickle
import sys

try:
    fileVar = sys.argv[1]
except IndexError:
    fileVar = ""

# Load pickle file
ideal_data = pickle.load(file('Pickles/' + fileVar))

x = ideal_data['Time']
y = ideal_data['Sensor Value']

# Plot
plt.plot(x,y)

# Properly format the x-labels
plt.gcf().autofmt_xdate()

# Show plot
plt.show()