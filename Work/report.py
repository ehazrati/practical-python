# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            name = record['name']
            nshares = int(record['shares'])
            price = float(record['price'])
            portfolio.append({'name': name, 'shares': nshares, 'price': price})

    return portfolio

def read_prices(filename):
    prices = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = ['name', 'price']
        for row in rows:
            if len(row) == 0:
                continue 

            record = dict(zip(headers, row))
            try:
               # record = dict(zip(headers, row))
                name = record['name']
                price = float(record['price'])
                prices[name] = price
            except IndexError:
                print('Bad row: ', row)
    return prices


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        name = stock['name']
        nshares = stock['shares']
        price = stock['price']
        current_price = prices[name]
        change = current_price - price
        report.append((name, nshares, price, change))
    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)



#if len(sys.argv) == 3:
#    portfolio_filename = sys.argv[1]
#    prices_filename = sys.argv[2]
#else:
#    portfolio_filename = input('Enter portfolio filename: ')
#    prices_filename = input('Enter prices filename: ')

portfolio_filename = 'Data/portfolio.csv' 
prices_filename = 'Data/prices.csv'



#portfolio = read_portfolio(portfolio_filename)
#prices = read_prices(prices_filename)

#report = make_report(portfolio, prices)
#print_report(report)

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report(portfolio_filename, prices_filename)




