import numpy_financial as npf
import pandas as pd
import numpy as np


def current_npv(rate=None, year=None):
    """ читаю и настраиваю датафэйм"""
    data = pd.read_excel("Расчет NPV.xlsx", index_col=0, sheet_name=1)

    if rate == None or year == None:
        rate = 0.2
        a = npf.npv(rate, data['доход'] - data['затраты'])
        return round(a, 2)

    else:
        data = data.loc[:year]
        a = npf.npv(float(rate), data['доход'] - data['затраты'])
        return round(a, 2)
