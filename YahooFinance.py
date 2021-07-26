# -*- coding: utf-8 -*-
"""
@author: Melisa Di Giacomo
"""

# Yahoo Finance: S&P 500 Index
# Show stock market crashes in the evaluated period of time

# Modules
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt


# Set the parameters to dowload Yahoo Finance data
# Yahoo Finance: S&P 500 Index
ticker = '^GSPC'
# Convert string to mktime
period1 = int(time.mktime(datetime.datetime.strptime("22/07/2016", "%d/%m/%Y").timetuple()))
period2 = int(time.mktime(datetime.datetime.strptime("22/07/2021", "%d/%m/%Y").timetuple()))
interval = '1d'

# Read data from web and create DataFrame
query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
df = pd.read_csv(query_string)

# Output data into CSV
df.to_csv('./YahooFinances_S&P500_5AÑOS.csv')

# Plot Price data
plt.style.use('ggplot')
ax = df.plot(x = "Date", y = 'Close',title ="S&P500 Index", fontsize=12, legend = False)
ax.set_xlabel("Date",fontsize=12)
ax.set_ylabel("Price",fontsize=12)
ax.annotate('COVID-19', xy=(914, 3450), xytext=(940, 3600),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("America's trade war with China", xy=(600, 2796), xytext=(630, 3100),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

