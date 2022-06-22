# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:07:31 2022

@author: Nhan Duong
"""

# Predicting stock prices with a Monte Carlo Simulation:

from import_data import import_data
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
    
company_list = ['PG', 'AMZN', 'AAPL', 'F']

def calculate_log_returns (df):
    return np.log(1 + df.pct_change())
   
def calculate_u(data):    
    return data.mean()
    
def calculate_var(data):
    return data.var()

def calculate_drift(x, y):
    return x - (0.5*y)

def calculate_std(data):
    return data.std()

def calculate_Z(days, iterations): 
    return norm.ppf(np.random.rand(days, iterations))
 
def calculate_daily_log_returns(a,b,c):
    return np.exp(a + b*c)
       
def predict_stock_price(series, my_data, days): 
    price_list = np.zeros_like(series)
    price_list[0] = my_data.iloc[-1]
    for t in range (1, days):
        price_list[t] = price_list[t-1]*series[t]
    return price_list
   
def plot_price_list(data, title):    
        plt.plot(data)
        plt.title(title)
        plt.show()
        
def calculate_min_price(data):
    return data.min()

def calculate_max_price(data):
    return data.max()

def calculate_average_price(data):
    return data.mean()

days = 100
iterations = 1000
simulated_prices = {}
S0s = {}
price_changes = {}
for company in company_list:
    closing_prices = import_data(company, '2020-1-1', '2022-5-31', 'Adj Close')
    log_returns = calculate_log_returns(closing_prices)
    u = calculate_u(log_returns)
    var = calculate_var(log_returns)
    drift = calculate_drift(u, var) 
    std = calculate_std(log_returns)
    Z = calculate_Z(days, iterations)
    daily_log_returns = calculate_daily_log_returns(drift, std, Z)
    price_list = predict_stock_price(daily_log_returns, closing_prices, days)
    plot_price_list(price_list, f'Stock Prices {company} after 100 days')
    minimum = calculate_min_price(price_list)
    maximum = calculate_max_price(price_list)
    mean = calculate_average_price(price_list)  
    S0 = closing_prices.iloc[-1]
    S0s[company] = S0
    if mean >= S0:
        print('gain')
        simulated_price = mean - S0
    else:
        print ('lost')
        simulated_price = S0 - mean
    simulated_prices[company]= simulated_price
    price_change = simulated_price/S0
    price_changes[company] = price_change
    


