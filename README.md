Actigraphy Analysis (Uploaded September 2021)

Author: Christopher Wang (christopher.wang@wustl.edu)

This code was developed in summer 2021 to analyze actigraphy (daily motor activity) data as part of human and mouse circadian biology research projects.
The program takes in a input .csv file containing data with the following columns: DATE (DD/MM/YYYY), TIME (XX:XX:XXX, 24 h), and ACTIVITY. 
This program can also take in .csv files containing Graph Data exported from ClockLab or .csv files with different names/orders of columns and different date formats.
This code was written in Python 3.8.1.

This code also uses the pyActigraphy library developed by Gregory Hammad (https://github.com/ghammad/pyActigraphy) to determine sleep and wake states at each timepoint using the MASDA (Roenneberg) and Cole-Kripke algorithms. Publication on pyActigraphy: https://pubmed.ncbi.nlm.nih.gov/34665807/ (Hammad et al. 2021)

This code currently calculates the following circadian rhythm metrics:
- M10
- Intradaily variability (IV)
- Interdaily stability (IS)
- Sleep-wake states using MASDA (pyActigraphy)
- Sleep-wake states using Cole-Kripke (pyActigraphy)
- Sleep onset time
- Sleep offset time
- Midsleep time
- Sleep bout number, timing, and duration
- Total sleep duration
- Sleep regularity index (SRI)
- Composite phase deviation (CPD)

Note: This code calculates CPD by using the mean midsleep over all days, not just free days.

References for sleep metric calculations:
- "Circadian rest-activity rhythm disturbances in Alzheimer's disease" - van Someren et al. (1996)
- "A novel method to visualise and quantify circadian misalignment" - Fischer, Vetter, Roenneberg (2016)
- "Irregular sleep/wake patterns are associated with poorer academic performance and delayed circadian and sleep/wake timing" - Phillips et al. (2017)
- "Measuring sleep regularity: theoretical properties and practical usage of existing metrics" - Fischer, Klerman, Phillips (2021)
- "pyActigraphy: Open-source python package for actigraphy data visualization and analysis" - Hammad et al. (2021)

USAGE INSTRUCTIONS:

1) If you do not have it already, install Python 3, which can be downloaded here: https://www.python.org/downloads/.

2) To run this code, download all .py files and place them in a folder together. Place all data files to be analyzed in a folder on the same level as the folder containing the .py files. For example: in the same parent folder, you can have one folder titled "Actigraphy Analysis Code" containing all of the .py files and another folder titled "Data Files" containing all of the .csv data files.

3) Run actigraphy_analysis.py using the command prompt or an IDE. The program will prompt you for the following inputs:
- Data format: Enter 1 if files have three columns in this order: Date (DD/MM/YYYY), Time, Activity; enter 2 if files are exported Graph Data from ClockLab; and enter 3 if .csv files have date, time, and activity columns out of order or if the date format is not DD/MM/YYYY.
- If you entered 3 above, the program will prompt you for the column names of the Date, Time, and Activity columns and also the date format.
- Whether the data are from diurnal (e.g. humans) or nocturnal (e.g. mice, rats) animals (enter D or N)
- Bin size (number of days) for multi-day metrics (IS, SRI)
- Name of the folder containing the data files

Sample data files are provided in the folders. The human test data is already in the default format (1), but it can also be run by using a custom format (3) and inputting DATE, TIME, and PIM for the column names and 1 for the date format (DD/MM/YYYY). The ClockLab data (exported by exporting Graph Data) can be analyzed by inputting 2 when the program prompts for data format.

4) For each data file, the code will automatically calculate all the metrics, along with correlations, p-values, and scatterplots, and export them to a newly created folder inside the folder containing the date.

If you encounter any errors, please email me at christopher.wang@wustl.edu letting me know what the error is, along with a sample data file that reproduces the error.
If you receive an error that says "KeyError" and you are using a custom file format, double-check that you are entering the column titles correctly.

Additionally, this code only works for data with 1-minute bins for activity counts. If you want to analyze data with a different bin size, please email me letting me know what bin size you would like, along with a sample data file so that I can test the program after editing it.
