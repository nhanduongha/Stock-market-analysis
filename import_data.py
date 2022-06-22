# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:42:33 2022

@author: Nhan Duong
"""

from pandas_datareader import data as wb


def import_data(symbols, start, end, prop):
    return wb.DataReader(symbols, data_source = 'yahoo', start = start, end = end)[prop]
