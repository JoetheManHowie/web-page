# Pandas: tips and tricks

On a day to day basis, I use the python library pandas in order to preform many of the data mining tasks I do.  Pandas is a wonderful library that a wide range of functionality, from operating similarly to a relational database to visualizing data driven results, the Pandas library allows for efficient data manipulation at scale in python.


The fundamental Object in the pandas library is `DataFrame`. As the name suggests, this class holds are data in a framework (or table) and has many methods for interacting with the dataset. A DataFrame, simply put, is a list columns with rows containing data entries for each column. For example say we are collecting temperature and pressure measurements in the Pacific Ocean. We want to know the temperature, pressure, location (longitude, latitude, and altitude), and the time the measurement was taken. So we have six column headers; temperature, pressure, longitude, latitude, altitude, and time. Suppose we survey 5 locations in the Pacific, then there is 5 rows in table of collected data. That is,

temperature | pressure | longitude | latitude | altitude | time
55.5 | 1021 | -140 | 46 | -100 | 07:00
56.5 | 1024 | -180 | 46 | -101 | 10:00
55.8 | 1022 | -140 | 56 | -97 | 12:00
54.5 | 1020 | -180 | 36 | -102 | 18:00
57.5 | 1025 | -140 | 36 | -99 | 20:00

*The units for temperature are Fahrenheit, kilo-Pascals for pressure, and meters below sea level for altitude. Note the data in the above table is made up whole cloth. We leave is as an exercise for the interested physics student to identify the inconsistencies. For instance, how fast would the boat have to travel in order to arrive at each location and carry out the measurements at the stated times? Or was the path taken by the surveyor's the most time efficient for the locations they visited?*

## Installing Pandas

To install the pandas library, use the pip package manager and type the following into your terminal

`pip install pandas`

## import Pandas

Like many popular python libraries it is common practice to import pandas with the alias pd.

`import pandas as pd`

## Reading Data into a Dataframe

The easiest way to read data into a DataFrame is to use `pd.read_csv()` which as the name suggests reads in data from a comma separated value file (like an excel table). Here is a short list of some methods to read data into a DataFrame:

+ `pd.read_csv()` See [the docs page for more details](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
+ `pd.read_pickle()` See [the docs page for more details](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_pickle.html)
+ `pd.read_html()` See [the docs page for more details](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html)

There are many more other file types, so take a look at [the docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/) for more on these methods.

## Building a DataFrame from Scratch

If you have your data already in a python script; because it is generated in your code; or stored as a series of lists; or in a python dictionary; then you can add it to a DataFrame directly by calling the object.

Using our example from above, suppose that we have six python list each with the measurements for the six columns. That is, the index of each list correspond to the row indices of the DataFrame we wish to build.

```python
!cat python_example_scripts/make_a_DataFrame.py
