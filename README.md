Project created April 13th, 2020
READEME file created April 23, 2020

Bikeshare Data Analysis tool
============================

Pre-requisites:
---------------
- Python 3
- NumbPy library
- Pandas library
- Matplotlib

Description:
------------
This project analyzes bike share data from three major cities

    - Washington DC
    - Chicago
    - New York City

The user must choose from one of these three cities to continue. Users will be prompted to select from the list of existing cities.

The user will then be prompted to select a month to filter by (or "all" to skip filtering by month), and a day of the week to filter by (or "all" to skip filtering by day of week).
NOTE: As there are a limited number of months available users will be prompted to select another month if data for that month is unavailable.

The following data will be returned based on the user's selections:
    - Most popular month for rentals
    - Most popular day of week for rentals
    - Most common hour of day for rentals
    - Most popular start, end, and combination of stations
    - Total and average trip durations
    - User types, gender, and birth year

Users will then be prompted to view data visualizations for several areas.

Once the above data is returned users will be able to view the complete row data 5 rows at a time. To view this data enter "y" when prompted. To quit the program enter "no" at the "Would you like to restart?" prompt.

Additional validation and error checking was added to prevent issues with missing data in certain .csv files.

### Files used
This project uses the following files:
    bikeshare_Oribello.py
    chicago.csv
    new_york_city.csv
    washington.csv

### Credits
Thanks to the Udacity team for initial technical knowledge and geeksforgeeks.com for additional information on material used in the validation areas.
