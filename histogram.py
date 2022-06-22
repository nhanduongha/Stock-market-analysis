# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:41:35 2022

@author: Nhan Duong
"""

from import_data import import_data
import matplotlib.pyplot as plt


company_list = ['PG', 'AMZN', 'AAPL', 'F']

    
def calculate_daily_return(data):
    return data.pct_change()

def plot_hist_daily_return(data, bins ,colour, title, file_name):
    plt.hist(data, bins = bins, color= colour)
    plt.xlabel('daily_return')
    plt.title(f'Daily return of {title}')
    plt.savefig(file_name)
    plt.show()


def program():
    for company in company_list:
        closing_prices = import_data(company, '2020-1-1', '2022-5-31', 'Adj Close')
        daily_return = calculate_daily_return(closing_prices)
        plot_hist_daily_return(daily_return, 100, 'green', company, f'Daily return of {company}') 

program()
