# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:10:05 2022

@author: Nhan Duong
"""

import numpy as np
import matplotlib.pyplot as plt

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
