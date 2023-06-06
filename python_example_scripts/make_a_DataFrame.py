#!/usr/bin/env python3

import pandas as pd

## data as a python list
temp =  [55.5, 56.5, 55.8, 54.5, 57.5]
pres = [1021, 1024, 1022, 1020, 1025]
long = [-140, -180, -140, -180, -140]
lati = [46, 46, 56, 36, 36]
alti = [-100, -101, -97, -102, -99]
time = ["07:00", "10:00", "12:00", "18:00", "20:00"]

## make a dictionary with keys the column names
data = {"temperature": temp,
        "pressure": pres,
        "longitude": long,
        "latitude": lati,
        "altitude": alti,
        "time": time}

## create DataFrame
df = pd.DataFrame(data)

## print table to terminal
print(df)
