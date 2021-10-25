Actigraphy Analysis (Uploaded September 2021)

Author: Christopher Wang (christopher.wang@wustl.edu)

This code was developed in summer 2021 to analyze actigraphy (daily motor activity) data as part of human and mouse circadian biology research projects.
The program takes in a input .csv file containing data with the following columns: DATE (DD/MM/YYYY), TIME (XX:XX:XXX, 24 h), and ACTIVITY.
Use of an actigraphy instrument that does not export data in this format will require an additional script to convert it to this format.

This code also uses the pyActigraphy library developed by Gregory Hammad (https://github.com/ghammad/pyActigraphy) to determine sleep and wake states at each timepoint using the MASDA (Roenneberg) and Cole-Kripke algorithms.

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
- Composite phase deviation (CPD
- Awakening number and duration during main sleep bout

To run this code, download all .py files and place them in a folder together. Place all data files to be analyzed in a folder on the same level as the folder containing the .py files.
Run actigraphy_analysis.py and, when prompted, enter the name of the folder containing the data files. The code will compute and export all metrics for each data file.
