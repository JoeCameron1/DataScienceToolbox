# Data Science Toolbox
This repository is a collection of python scripts and tools I used regularly to perform my role as a data scientist. 
The code was written to analyse and obtain information on the IDEAL dataset, a household energy usage dataset created by the University of Edinburgh.
The dataset, and more information on it, can be found here: [IDEAL Dataset](https://datashare.is.ed.ac.uk/handle/10283/3647).

---------------

Although written with a certain dataset in mind, the core process of analysis and subsequent visualisation can be replicated on other datasets with a few minor tweaks to the code.

---------------

Below are some examples of the figures produced by some of the scripts in this repository:

| An example of a figure produced by [dailyEnergyAverage.py](dailyEnergyAverage.py) |
|------|
|![dailyEnergyAverage.py Example Figure](/ExampleFigures/dailyEnergyAverageExample.png)| 

| An example of a figure produced by [showTimeGaps.py](showTimeGaps.py) |
|------|
|![showTimeGaps.py Example Figure](/ExampleFigures/showTimeGapsExample.png)|

| An example of a figure produced by [seasonalAverage.py](seasonalAverage.py) |
|------|
|![seasonalAverage.py Example Figure](/ExampleFigures/seasonalAverageExample.png)|

| An example of a figure produced by [consumption.py](consumption.py) |
|------|
|![consumption.py Example Figure](/ExampleFigures/consumptionExample.png)|

| An example of a figure produced by [total-robust-consumption.py](total-robust-consumption.py) |
|------|
|![total-robust-consumption.py Example Figure](/ExampleFigures/total-robust-consumptionExample.png)|

---------------

Every file is documented with its own description and correct use in the command line.
Additionally, the table below quickly summarises the purpose and correct usage of each file:
| File                            | Description | Usage |
|:--------------------------------|:---|:---|
| [boxplot-percentiles.py](boxplot-percentiles.py)          | Same as total-boxplot-consumption.py, except this script prints the percentiles that are otherwise displayed in total-boxplot-consumption.py. | python boxplot-percentiles.py [-d/-g/-w] data.csv |
| [combine.py](combine.py)                      | Combines gas and electricity data from .csv files into an overall energy csv file and saves it. Can also display and save figures showing total energy usage. | python combine.py gasData.csv electricityData.csv |
| [consumption.py](consumption.py)                  | Displays total energy consumption sum over a dataset's lifetime for every given hour during a day, given day, given week and given month. | python consumption.py [-d/-g/-w/-m] data.csv |
| [dailyAverage.py](dailyAverage.py)                 | Produces the average value for every hour/minute/second during the day over all available datetime data. Can also display and save figures showing the average values as a boxplot or line graph. Further ability to save pickles for later data retrieval. | python dailyAverage.py [-d/-m/-s] [-b/-n] data.csv |
| [dailyEnergyAverage.py](dailyEnergyAverage.py)           | Same as dailyAverage.py, although this is tailored for energy consumption in Wh. | python dailyEnergyAverage.py [-d/-m/-s] [-b/-n] data.csv |
| [dailyEnergySum.py](dailyEnergySum.py)               | Produces the daily sum of total energy usage over all available datetime data. Can also display and save figures showing the sum values as a line graph. Further ability to save pickles for later data retrieval. | python dailyEnergySum.py data.csv |
| [dataVis.py](dataVis.py)                      | Visualises all data from csv files in a directory of the IDEAL dataset. For every .csv file in a directory, a figure and pickle is saved in the subdirectories 'Figures/' and 'Pickles/' | Navigate to directory with .csv files and type 'python dataVis.py' |
| [display.py](display.py)                      | Same as dataVis.py. Originally used to visualise on a single .csv file with raw data. | Navigate to directory with .csv files and type 'python display.py' |
| [displayASHP.py](displayASHP.py)                  | Save/Display the electricity needs of an Air Source Heat Pump to generate equivalent heat given by gas. | python displayASHP.py gasData.csv |
| [displayElectric.py](displayElectric.py)              | Display raw electric data from the IDEAL dataset as a line graph. Can also save the graph in a 'ElectricFigures/' directory. | python displayElectric.py electricData.csv |
| [displayEnergy.py](displayEnergy.py)                | Saves and shows csv data and figures that show a user's total energy usage from gas and electricity data in 'EnergyCSV/' and 'EnergyFigures/' folders. | python displayEnergy.py gasData.csv electricityData.csv |
| [displayGas.py](displayGas.py)                   | Display raw gas data from the IDEAL dataset as a line graph. Can also save the graph in a 'GasFigures/' directory. | python displayGas.py gasData.csv |
| [formatCSV.py](formatCSV.py)                    | Prints each and every raw IDEAL data .csv file within a directory as a string. | Navigate to directory with .csv files and type 'python formatCSV.py' |
| [monthlyEnergyAverage.py](monthlyEnergyAverage.py)         | Same as dailyEnergyAverage.py, except this script also saves the average values within the timeframe of each month (rather than the whole range of available datetime data) in a separate .csv file in a directory called 'MonthlyAveEnergyCSV/'. | python monthlyEnergyAverage.py [-d/-m/-s] [-b/-n] data.csv |
| [monthlyOverallEnergyAverage.py](monthlyOverallEnergyAverage.py)  | Same as monthlyEnergyAverage.py, except this script saves the average hourly values (for each month's timeframe) from all .csv files in a directory rather than just a single .csv file. | python monthlyOverallEnergyAverage.py [-b/-n] |
| [overallEnergyAverage.py](overallEnergyAverage.py)         | Gives average daily energy demand curves from all aggregated users. Uses data given by the dailyEnergyAverage.py script. | python overallEnergyAverage.py [-b/-n] |
| [preprocessElectric-30.py](preprocessElectric-30.py)        | Saves electricity data in Watt Hours instead of Watts (as it was originally measured for the IDEAL dataset). Rounded to the nearest 30 minutes. | python preprocessElectric-30.py electricityData.csv |
| [preprocessElectric-Hour.py](preprocessElectric-Hour.py)      | Saves electricity data in Watt Hours instead of Watts (as it was originally measured for the IDEAL dataset). Rounded to the nearest hour. | python preprocessElectric-Hour.py electricityData.csv |
| [preprocessElectric.py](preprocessElectric.py)           | Saves electricity data in Watt Hours instead of Watts (as it was originally measured for the IDEAL dataset). No rounding. | python preprocessElectric.py electricityData.csv |
| [preprocessGas-30.py](preprocessGas-30.py)             | Saves clean gas data with boiler efficiency and coefficient of performance (COP) values accounted for. Rounded to the nearest 30 minutes. | python preprocessGas-30.py gasData.csv |
| [preprocessGas-Hour.py](preprocessGas-Hour.py)           | Saves clean gas data with boiler efficiency and coefficient of performance (COP) values accounted for. Rounded to the nearest hour. | python preprocessGas-Hour.py gasData.csv |
| [preprocessGas.py](preprocessGas.py)                | Saves clean gas data with boiler efficiency and coefficient of performance (COP) values accounted for. No rounding. | python preprocessGas.py gasData.csv |
| [seasonalAverage.py](seasonalAverage.py)              | Produces the average value for every hour/minute/second during the day, for each season (Winter, Spring, Summer, Autumn). Can also display and save figures showing the average values as a boxplot or line graph. Further ability to save pickles for later data retrieval. | python seasonalAverage.py [-d/-m/-s] [-b/-n] data.csv |
| [showFig.py](showFig.py)                      | Shows a figure from data stored in a pickle file. The file is given as a command-line argument. | python showFig.py pickleFile.pkl |
| [showTimeGaps.py](showTimeGaps.py)                 | Looks for time gaps within the data and produces a graph to show how many gaps of varying sizes occur within the dataset. | python showTimeGaps.py data.csv |
| [smoothedDailyEnergyAverage.py](smoothedDailyEnergyAverage.py)   | Same as dailyEnergyAverage.py, except this script also applies median smoothing to the data before visualisation. | python smoothedDailyEnergyAverage.py [-d/-m/-s] [-b/-n] data.csv |
| [smoothedOverallEnergyAverage.py](smoothedOverallEnergyAverage.py) | Same as overallEnergyAverage.py, except this script uses smoothed data from smoothedDailyEnergyAverage.py. | python smoothedOverallEnergyAverage.py [-b/-n] |
| [total-boxplot-consumption.py](total-boxplot-consumption.py)    | Displays a boxplot of energy consumption for every month, where data is resampled by hour, day and week. Takes either gas data or electricity data. | python total-boxplot-consumption.py [-d/-g/-w] data.csv |
| [total-robust-consumption.py](total-robust-consumption.py)     | Displays energy consumption sum for every hour, day, week and month. Takes gas and electricity data. | python total-robust-consumption.py [-d/-g/-w/-m] gasData.csv electricityData.csv |
