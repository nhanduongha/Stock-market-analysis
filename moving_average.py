# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:41:35 2022

@author: Nhan Duong
"""

from import_data import import_data
import matplotlib.pyplot as plt
import pandas as pd
from stock_market import plot_closing_prices

company_list = ['PG', 'AMZN', 'AAPL', 'F']
ma_day = [10, 50]


   
def calculate_moving_average(series, ma_day):
    moving_averages = []
    for ma in ma_day:
        moving_averages.append(series.rolling(ma).mean())
    return pd.concat(moving_averages, axis=1, keys=ma_day)


def plot_moving_average(df1, df2, title, file_name):
    df1.plot(figsize=(15,7), title=title)
    df2.plot(figsize=(15,7), title=title)
    plt.legend(loc='upper left')
    plt.title(title)
    plt.savefig(file_name)
    plt.show()

def program():
    for company in company_list:
        closing_prices = import_data(company, '2020-1-1', '2022-5-31', 'Adj Close')
        moving_average = calculate_moving_average(closing_prices, ma_day)
        plot_closing_prices(closing_prices, 'Closing Price', 'Closing Price.png')
        plot_moving_average(moving_average,closing_prices, f'{company} moving average', f'{company} Moving average.png')
program()