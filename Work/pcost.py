# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    for row in rows:
        try: 
            nshares = int(row[1])
            price = float(row[2])
            total_cost = total_cost + nshares * price
        except ValueError:
            print('Bad row: ', row)

        total_cost = total_cost + nshares * price
    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else: 
    filename = input('Enter a file name:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
