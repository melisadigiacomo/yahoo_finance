# -*- coding: utf-8 -*-
"""
@author: Melisa Di Giacomo
"""

#%%

# Modules
import time
import datetime
import pandas as pd
import plotly.express as px

#%% WEBSCRAPING YAHOO FINANCE DATA

# Set the parameters to dowload Yahoo Finance data
# Yahoo Finance: historical prices
ticker = 'TSLA'
# Convert string to mktime
period1 = int(time.mktime(datetime.datetime.strptime("01/10/2021", "%d/%m/%Y").timetuple()))
period2 = int(time.mktime(datetime.datetime.strptime("25/10/2021", "%d/%m/%Y").timetuple()))
interval = '1d'

# Read data from web and create DataFrame
query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
df = pd.read_csv(query_string)

# Output data into CSV
df.to_csv('./YahooFinances_TSLA.csv')

#%% DATA ANALYSIS

# Read DataFrame stocks of popular companies
df = pd.read_csv('./Stocks_Companies_YahooFinance.csv', header = 0)
df.head(10)


# Animated pairplot of popular companies: Adj Close vs Volume.
# Circle size based on Volume. Color key for different companies.
px.scatter(data_frame = df,
           x = 'Adj Close',
           y= 'Volume',
           size = 'Volume',
           color = 'Company',
           title = 'Volume vs Adj Close',
           # Scales
           range_x = [-500, 4000],
           range_y = [-20e+06, 15e+07],          
           # Company when hover over points
           hover_name = 'Company',
           text = "Company",
           # Animation based on date
           animation_frame = 'Date',
           size_max = 100)


# Animated pairplot of popular companies: % Daily Return vs Volume.
# Circle size based on Volume. Color key for different companies.
px.scatter(data_frame = df,
           x = 'Volume',
           y= '% Daily Return',
           size = 'Volume',
           color = 'Company',
           title = '% Daily Return vs Volume',
           # Scale
           range_y = [-15,20],
           range_x = [-20e+06, 12e+07], 
           # Company when hover over points
           hover_name = 'Company',
           text = "Company",
           # Animation based on date
           animation_frame = 'Date',
           size_max = 100)


#%% Tesla, Inc.

df_TSLA = df.where(df.Company == 'TSLA').dropna()
df_TSLA.head(10)
df_TSLA.describe()


# Pairplot: % Daily Return vs Volume of Tesla, Inc.
px.scatter(data_frame = df_TSLA,
           x = 'Date',
           y= 'Volume',
           size = 'Volume',
           color = '% Daily Return',
           title = 'TSLA: Date vs Volume - Octuber',
           # Company when hover over points
           hover_name = 'Company',
           text = '% Daily Return',
           color_continuous_scale = 'sunset',
           size_max = 100)


#%% Stocks of popular companies on October 25, 2021.

df_25 = df.where(df.Date == '10/25/2021').dropna()
df_25.head(10)


# Pairplot: Volume vs % Daily Return of popular companies on Octuber 25, 2021.
# Circle size based on Volume. Color key for different companies.
px.scatter(data_frame = df_25,
           x = 'Volume',
           y= '% Daily Return',
           size = 'Volume',
           color = 'Company',
           title = 'Volume vs % Daily Return - Octuber 25, 2021',
           # Company when hover over points
           hover_name = 'Company',
           text = "Company",
           size_max = 100)


#%% Pairplot: Company vs Volume on Octuber 25, 2021.
# Circle size based on Volume. Color key for % Daily Return.
px.scatter(data_frame = df_25,
           x = 'Company',
           y= 'Volume',
           size = 'Volume',
           color = '% Daily Return',
           title = 'Company vs Volume - Octuber 25, 2021',
           # Company when hover over points
           hover_name = 'Company',
           text = '% Daily Return',
           color_continuous_scale = 'sunset',
           size_max = 100)