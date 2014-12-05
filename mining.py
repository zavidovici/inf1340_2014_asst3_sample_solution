#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

# MONTHY_V_C :
# dict mapping "%Y/%m" date strings to
# a list of (volume, cost) tuples
MONTHLY_V_C = {}

# MONTHY_AVGS :
# list of 2-tuples: "%Y/%m" date
# and a monthly average
MONTHLY_AVGS = []

def read_stock_data(stock_name, stock_file_name):
    """
    Populate MONTHLY_V_C dictionary.

    This dictionary maps dates (strings in the format "%Y/%m")
    to a list of (volume, cost) tuples.
    """

    with open(stock_file_name) as f:
        stock_prices = json.load(f)

    # store daily volume and close numbers in MONTHLY_V_C
    for stock_dict in stock_prices:
        # parse date
        p_date = datetime.datetime.strptime(stock_dict["Date"], '%Y-%m-%d')
        date = str(p_date.year) + '/' + str(p_date.month)

        v = stock_dict['Volume']
        c = stock_dict['Close']
        if date not in MONTHLY_V_C:
            MONTHLY_V_C[date] = [(v,c)]
        else:
            MONTHLY_V_C[date].append((v,c))

    # compute average
    for month,l in MONTHLY_V_C.items():
        avg = sum([v*c for (v,c) in l]) / sum([v for (v,c) in l])
        MONTHLY_AVGS.append((month, avg))

    # sort MONTHLY_AVGS by value of average
    MONTHLY_AVGS.sort(key=lambda t: t[1], reverse=True)


def six_best_months():
    """
    Return the six best months as a list of (month, average)
    tuples, where month is a string in the format "%Y/%m".
    """
    return MONTHLY_AVGS[:6]


def six_worst_months():
    """
    Return the six worst months as a list of (month, average)
    tuples, where month is a string in the format "%Y/%m".
    """
    return MONTHLY_AVGS[-6:][::-1]

