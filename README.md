# Data Science Toolbox
This repository is a collection of python scripts and tools I used regularly to perform my role as a data scientist. 
The code was written to analyse and obtain information on the IDEAL dataset, a household energy usage dataset created by the University of Edinburgh.
The dataset, and more information on it, can be found here: [IDEAL Dataset](https://datashare.is.ed.ac.uk/handle/10283/3647).

---------------

Although written with a certain dataset in mind, the core process of analysis and subsequent visualisation can be replicated on other datasets with a few minor tweaks to the code.

---------------

Every file is documented with its own description and correct use in the command line.
Additionally, the table below quickly summarises the purpose and correct usage of each file:
| File                            | Description | Usage |
|:--------------------------------|:---|:---|
| combine.py                      | Combines gas and electricity data from .csv files into an overall energy csv file and saves it. Can also display and save figures showing total energy usage. | python combine.py gasData.csv electricityData.csv |
| dailyAverage.py                 | Produces the average value for every hour/minute/second during the day over all available datetime data. Can also display and save figures showing the average values as a boxplot or line graph. Further ability to save pickles for later data retrieval. | python dailyAverage.py [-d/-m/-s] [-b/-n] data.csv |
| dailyEnergyAverage.py           | Same as dailyAverage.py, although this is tailored for energy consumption in Wh. | python dailyEnergyAverage.py [-d/-m/-s] [-b/-n] data.csv |
| dailyEnergySum.py               | Produces the daily sum of total energy usage over all available datetime data. Can also display and save figures showing the sum values as a line graph. Further ability to save pickles for later data retrieval. | python dailyEnergySum.py data.csv |
| dataVis.py                      | Visualises all data from csv files in a directory of the IDEAL dataset. For every .csv file in a directory, a figure and pickle is saved in the subdirectories 'Figures/' and 'Pickles/' | Navigate to directory with .csv files and type 'python dataVis.py' |
| display.py                      | Same as dataVis.py. Originally used to visualise on a single .csv file with raw data. | Navigate to directory with .csv files and type 'python display.py' |
| displayASHP.py                  | Save/Display the electricity needs of an Air Source Heat Pump to generate equivalent heat given by gas. | python displayASHP.py gasData.csv |
| displayElectric.py              | Display raw electric data from the IDEAL dataset as a line graph. Can also save the graph in a 'ElectricFigures/' directory. | python displayElectric.py electricData.csv |
| displayEnergy.py                | Saves and shows csv data and figures that show a user's total energy usage from gas and electricity data in 'EnergyCSV/' and 'EnergyFigures/' folders. | python displayEnergy.py gasData.csv electricityData.csv |
| displayGas.py                   | Display raw gas data from the IDEAL dataset as a line graph. Can also save the graph in a 'GasFigures/' directory. | python displayGas.py gasData.csv |
| formatCSV.py                    | Prints each and every raw IDEAL data .csv file within a directory as a string. | Navigate to directory with .csv files and type 'python formatCSV.py' |
| monthlyEnergyAverage.py         | Same as dailyEnergyAverage.py, except this script also saves the average values within the timeframe of each month (rather than the whole range of available datetime data) in a separate .csv file in a directory called 'MonthlyAveEnergyCSV/'. | python monthlyEnergyAverage.py [-d/-m/-s] [-b/-n] data.csv |
| monthlyOverallEnergyAverage.py  | Same as monthlyEnergyAverage.py, except this script saves the average hourly values (for each month's timeframe) from all .csv files in a directory rather than just a single .csv file. | python monthlyOverallEnergyAverage.py [-b/-n] |
| overallEnergyAverage.py         | Gives average daily energy demand curves from all aggregated users. Uses data given by the dailyEnergyAverage.py script. | python overallEnergyAverage.py [-b/-n] |
| preprocessElectric-30.py        | Saves electricity data in Watt Hours instead of Watts (as it was originally measured for the IDEAL dataset). Rounded to the nearest 30 minutes. | python preprocessElectric-30.py electricityData.csv |
| preprocessElectric-Hour.py      | Saves electricity data in Watt Hours instead of Watts (as it was originally measured for the IDEAL dataset). Rounded to the nearest hour. | python preprocessElectric-Hour.py electricityData.csv |
| preprocessElectric.py           | Saves electricity data in Watt Hours instead of Watts (as it was originally measured for the IDEAL dataset). No rounding. | python preprocessElectric.py electricityData.csv |
| preprocessGas-30.py             | Saves clean gas data with boiler efficiency and coefficient of performance (COP) values accounted for. Rounded to the nearest 30 minutes. | python preprocessGas-30.py gasData.csv |
| preprocessGas-Hour.py           | Saves clean gas data with boiler efficiency and coefficient of performance (COP) values accounted for. Rounded to the nearest hour. | python preprocessGas-Hour.py gasData.csv |
| preprocessGas.py                | Saves clean gas data with boiler efficiency and coefficient of performance (COP) values accounted for. No rounding. | python preprocessGas.py gasData.csv |
| seasonalAverage.py              |  |  |
| showFig.py                      |  |  |
| showTimeGaps.py                 |  |  |
| smoothedDailyEnergyAverage.py   |  |  |
| smoothedOverallEnergyAverage.py |  |  |
| total-boxplot-consumption.py    |  |  |
| total-robust-consumption.py     |  |  |
