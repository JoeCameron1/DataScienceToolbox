# Data Science Toolbox
This repository is a collection of python scripts and tools I used regularly to perform my role as a data scientist. 
The code was written to analyse and obtain information on the IDEAL dataset, a household energy usage dataset created by the University of Edinburgh.
The dataset, and more information on it, can be found here: [IDEAL Dataset](https://datashare.is.ed.ac.uk/handle/10283/3647).

Although written with a certain dataset in mind, the core process of analysis and subsequent visualisation can be replicated on other datasets with a few minor tweaks to the code.

Every file is documented with its own description and correct use in the command line.
Additionally, the table below quickly summarises the purpose and correct usage of each file:
| File                            | Description | Usage |
|:-------------------------------:|:---:|:---|
| combine.py                      | Combines gas and electricity data from .csv files into an overall energy csv file and saves it. Can also display and save figures showing total energy usage. | python combine.py gasData.csv electricityData.csv |
| dailyAverage.py                 | Produces the average value for every hour/minute/second during the day over all available datetime data. Can also display and save figures showing the average values as a boxplot or line graph. | python dailyAverage.py -d/-m/-s -b/-n data.csv |
| dailyEnergyAverage.py           |  |  |
| dailyEnergySum.py               |  |  |
| dataVis.py                      |  |  |
| display.py                      |  |  |
| displayASHP.py                  |  |  |
| displayElectric.py              |  |  |
| displayEnergy.py                |  |  |
| displayGas.py                   |  |  |
| formatCSV.py                    |  |  |
| monthlyEnergyAverage.py         |  |  |
| monthlyOverallEnergyAverage.py  |  |  |
| overallEnergyAverage.py         |  |  |
| preprocessElectric-30.py        |  |  |
| preprocessElectric-Hour.py      |  |  |
| preprocessElectric.py           |  |  |
| preprocessGas-30.py             |  |  |
| preprocessGas-Hour.py           |  |  |
| preprocessGas.py                |  |  |
| seasonalAverage.py              |  |  |
| showFig.py                      |  |  |
| showTimeGaps.py                 |  |  |
| smoothedDailyEnergyAverage.py   |  |  |
| smoothedOverallEnergyAverage.py |  |  |
| total-boxplot-consumption.py    |  |  |
| total-robust-consumption.py     |  |  |
