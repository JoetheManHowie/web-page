# Pandas: tips and tricks

On a day to day basis, I use the python library pandas in order to preform many different data mining tasks.  Pandas is a wonderful library that a wide range of functionality, from operating similarly to a relational database to visualizing data driven results, the Pandas library allows for efficient data manipulation at scale in python.


The fundamental Object in the pandas library is `DataFrame`. As the name suggests, this class holds are data in a framework (or table) and has many methods for interacting with the dataset. A DataFrame, simply put, is a list columns with rows containing data entries for each column. For example say we are collecting temperature and pressure measurements in the Pacific Ocean. We want to know the temperature, pressure, location (longitude, latitude, and altitude), and the time the measurement was taken. So we have six column headers; temperature, pressure, longitude, latitude, altitude, and time. Suppose we survey 5 locations in the Pacific, then there is 5 rows in table of collected data. That is,

| temperature | pressure | longitude | latitude | altitude | time |
|--------------|-----------|------------|-------------|-----------|------------|
| 55.5 | 1021 | -140 | 46 | -100 | 07:00 |
| 56.5 | 1024 | -180 | 46 | -101 | 10:00 |
| 55.8 | 1022 | -140 | 56 | -97 | 12:00 |
| 54.5 | 1020 | -180 | 36 | -102 | 18:00 |
| 57.5 | 1025 | -140 | 36 | -99 | 20:00 |

*The units for temperature are Fahrenheit, kilo-Pascals for pressure, and meters below sea level for altitude. Note the data in the above table is made up whole cloth. We leave is as an exercise for the interested physics student to identify the inconsistencies. For instance, how fast would the boat have to travel in order to arrive at each location and carry out the measurements at the stated times? Or was the path taken by the surveyor's the most time efficient for the locations they visited?*

## Installing Pandas

To install the pandas library, use the pip package manager and type the following into your terminal

`pip install pandas`

## Import Pandas

Like many popular python libraries it is common practice to import pandas with the alias pd.

`import pandas as pd`

## Reading Data into a Dataframe

The easiest way to read data into a DataFrame is to use `pd.read_csv()` which as the name suggests reads in data from a comma separated value file (like an excel table). Here is a short list of some methods to read data into a DataFrame, and below we give examples with our temperature data on how to use them.

####  Read from csv
A csv (or comma separated value) file that contains our temperature example can be [downloaded here.](https://joehowie.ca/xample_scripts/temperature_data.csv) With the data downloaded, you can now load it into a pandas DataFrame running the following python code.
```python
import pandas as pd

column_names = ["temperature", "pressure", "longitude", "latitude", "altitude", "time"] # column names, as they are not in the file itself
df = pd.read_csv("temperature_data.csv", names=column_names) # load data with the column names passed in
print(df)
```
See [the docs page for more details on using `pd.read_csv()`.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

### Read from html

Given that most of the world wide web consists of html pages, you are bound to run into to these table soon or later. We have prepared the temperature example data in a html format [downloadable here.](https://joehowie.ca/example_scripts/temperature_data.html). Now that the data has been downloaded the following code can be executed to read the table into a pandas DataFrame.

```python
import pandas as pd

# Read the HTML file and obtain a list of DataFrame objects
dataframes = pd.read_html("temperature_data.html")
# Access the desired DataFrame object (assuming it's the first one)
df = dataframes[0]
# Specify the column names
df.columns = column_names
print(df)
```
See [the docs page for more details on `pd.read_html()`.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html)

### Read from pickle

Pickle is a python module for serializing map data structures like dictionaries and json data. If you have data stored as a python dictionary, you may save that data to a pickle file for later use in a separate program. The temperature data has been serialized using the python pickler (which is fun to say five times fast) and can be [downloaded from this link](https://joehowie.ca/example_scripts/temperature_data.pkl)

See [the docs page for more details on `pd.read_pickle()`.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_pickle.html)


all three code snippets will print the following result:

```yaml
temperature  pressure  longitude  latitude  altitude   time
0         55.5      1021       -140        46      -100  07:00
1         56.5      1024       -180        46      -101  10:00
2         55.8      1022       -140        56       -97  12:00
3         54.5      1020       -180        36      -102  18:00
4         57.5      1025       -140        36       -99  20:00
```
There are many more other file types, so take a look at [the docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/) for more on these methods. Below we give examples for importing data using the three methods above.


## Building a DataFrame from Scratch

If you have your data already in a python script; because it is generated in your code; or stored as a series of lists; or in a python dictionary; then you can add it to a DataFrame directly by calling the object.

Using our example from above, suppose that we have six python list each with the measurements for the six columns. That is, the index of each list correspond to the row indices of the DataFrame we wish to build.

```python
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
```

## Adding data to a Dataframe

Once you have a DataFrame like in the above code block, you can add rows using `pd.concat`.
