#!/usr/bin/env python3

import pandas as pd

def print_type(dd):
    df = dd.iloc[0]
    print(type(df.temperature), type(df.pressure), type(df.longitude), type(df.latitude), type(df.latitude), type(df.altitude), type(df.time))
    print(dd)


## data as a python list
temp =  [55.5, 56.5, 55.8, 54.5, 57.5]
pres = [1021, 1024, 1022, 1020, 1025]
long = [-140, -180, -140, -180, -140]
lati = [46, 46, 56, 36, 36]
alti = [-100, -101, -97, -102, -99]
time = ["07:00", "10:00", "12:00", "18:00", "20:00"]

## make a dictionary with keys the column names
print("From Dictionary")
data = {"temperature": temp,
        "pressure": pres,
        "longitude": long,
        "latitude": lati,
        "altitude": alti,
        "time": time}

## create DataFrame
df = pd.DataFrame(data)
print_type(df)
## print table to terminal
#####################

# Adding from lists
print("From List")
# Data as a 2D list
data = [
    [55.5, 1021, -140, 46, -100, "07:00"],
    [56.5, 1024, -180, 46, -101, "10:00"],
    [55.8, 1022, -140, 56, -97, "12:00"],
    [54.5, 1020, -180, 36, -102, "18:00"],
    [57.5, 1025, -140, 36, -99, "20:00"]
]

# Column names
column_names = ["temperature", "pressure", "longitude", "latitude", "altitude", "time"]

# Create DataFrame
df = pd.DataFrame(data, columns=column_names)
print_type(df)
# Print table to terminal

###################
print("Adding a row to the bottom")
### Adding rows one at a times
new_row_entry = [[55.1, 1021, -150, 40, -102, "22:00"]]

# we use the class variable `columns` to get the names of the columns in df.
new_row = pd.DataFrame(new_row_entry, columns=df.columns)#list(data.keys()))

# appedn the new row to the bottom
df = pd.concat([df, new_row], ignore_index=True)
print_type(df)
#######################
print("From csv")
## Read data from a csv
df = pd.read_csv("temperature_data.csv", names=column_names)
print_type(df)
################
print("From HTML")
# Read the HTML file and obtain a list of DataFrame objects
dataframes = pd.read_html("temperature_data.html")

# Access the desired DataFrame object (assuming it's the first one)
df = dataframes[0]

# Specify the column names
df.columns = column_names

print_type(df)
###############


## Check types
