# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:27:25 2022

@author: Nhan Duong
"""

from import_data import import_data
from stock_market import (calculate_daily_return, 
                          calculate_average_daily_return,
                          calculate_cov_matrix)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


company_list = ['PG', 'AMZN', 'AAPL', 'F']

num_companies = len(company_list)
num_portfolios = 2000
portfolio_returns = []
portfolio_volatilities = []
company_weights = []

def calculate_weight(number):
    weight = np.random.random(number)
    weight /= np.sum(weight)
    return weight

def calculate_returns(number, data):     
    return np.sum(number*data)*250
       
def calculate_volatilities(number, matrix):    
    return np.sqrt(np.dot(number.T,np.dot(matrix,number)))     
        
def plot_efficient_frontier(df, x_label, y_label, title, file_name):    
    df.plot(x='Volatility', y='Return', kind= 'scatter', figsize = (10,6))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(file_name)
    plt.show()

closing_prices = import_data(company_list, '2020-1-1', '2022-5-31', 'Adj Close')
daily_return = calculate_daily_return(closing_prices)
average_daily_return = calculate_average_daily_return(daily_return)
cov_matrix = calculate_cov_matrix(daily_return)
for x in range(num_portfolios):
    weight = calculate_weight(num_companies)
    returns = calculate_returns(weight, average_daily_return)
    volatilities = calculate_volatilities(weight, cov_matrix)
    portfolio_returns.append(returns)
    portfolio_volatilities.append(volatilities)
    new_weights = {x: weight[i] for i, x in enumerate(company_list)}
    company_weights.append(new_weights)

portfolios = pd.DataFrame({'Weight': company_weights,
                           'Return': portfolio_returns,
                           'Volatility': portfolio_volatilities})

plot_efficient_frontier(portfolios,'Expected Volatility', \
                                'Expected Return', 'The efficient frontier', \
                                    'The efficient frontier')
