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
        for row in rows:
            name = row[0]
            nshares = int(row[1])
            price = float(row[2])
            portfolio.append({'name': name, 'shares': nshares, 'price': price})

    return portfolio

def read_prices(filename):
    prices = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try: 
                name = row[0]
                price = float(row[1])
                prices[name] = price
            except IndexError:
                print('Bad row: ', row)
    return prices

if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = input('Enter portfolio filename: ')
    prices_filename = input('Enter prices filename: ')

portfolio = read_portfolio(portfolio_filename)
prices = read_prices(prices_filename)

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares'] * prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)

