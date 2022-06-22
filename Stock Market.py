# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:58:36 2022

@author: Nhan Duong
"""

import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import dataframe_image as dfi


company_list = ['PG', 'AMZN', 'AAPL', 'F']
ma_day = [10, 50]


def import_data(symbols, start, end, prop):
    return wb.DataReader(symbols, data_source = 'yahoo', start = start, end = end)[prop]

def summarise_statistic_values(data):
    return data.describe()

def plot_closing_prices(df, title, file_name):
    df.plot(figsize=(15,7), title = title)
    plt.savefig(file_name)
    
def calculate_daily_return(data):
    return data.pct_change()

def calculate_average_daily_return(data2):
    return data2.mean()

def plot_daily_return(data, label, file_name):
    data.plot(figsize=(15,7), label=label)
    plt.legend(loc='upper right')
    plt.title('Daily return')
    plt.savefig(file_name)
    plt.show()  

def calculate_standard_deviation(df):
    return df.std()

def calculate_portfolio_return(data, weights):
    return (weights * data).sum()

def calculate_cov_matrix(data):
    return data.cov()*250

def calculate_portfolio_var(figures,weights):
    weights = np.array([0.15,0.2,0.25,0.4])
    return np.dot(weights.T,np.dot(figures,weights))

def calculate_portfolio_risk(number):
    portfolio_volatility = np.sqrt(number)
    print(str(round(portfolio_volatility,4)*100) + '%')  
    return portfolio_volatility

def calculate_sharpe_ratio(x, rf, y): 
    return (x - rf) / y *(250**0.5)
    
closing_prices = import_data(company_list, '2020-1-1', '2022-5-31', 'Adj Close')
summary_statistic = summarise_statistic_values(closing_prices)
plot_closing_prices(closing_prices, 'Closing Price', 'Closing Price.png')
daily_return = calculate_daily_return(closing_prices)
average_daily_return = calculate_average_daily_return(daily_return)
plot_daily_return(daily_return, company_list, 'Daily return.png')
std = calculate_standard_deviation(daily_return)
weights = [0.15,0.2,0.25,0.4]
return_portfolio = calculate_portfolio_return(average_daily_return, weights)
cov_matrix = calculate_cov_matrix(daily_return)
portfolio_var = calculate_portfolio_var(cov_matrix, weights)
portfolio_volatility = calculate_portfolio_risk(portfolio_var)
rf = 0.0166
sharpe_ratio = calculate_sharpe_ratio(return_portfolio,rf, portfolio_volatility)

dfi.export(summary_statistic, 'Summary_statistic.png')
dfi.export(cov_matrix, 'cov_marix.png')