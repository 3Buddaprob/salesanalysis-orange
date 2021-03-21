import csv
from typing import List

data=[]

with open('sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
    #return data

sales = []
for row in data:
    sale = int(row['sales'])
    sales.append(sale)

expenditures=[]

for row in data:
    expenditure = int(row['expenditure'])
    expenditures.append(expenditure) #collect expenditures
    
total_s = sum(sales)
total_ex = sum(expenditures)
print(f'total sales:{total_s}') #output total sales
print(f'total expenditures: {total_ex}')

for row in data:
    print "In row {}s, Max = {}s" .format(index, max(row))

for row in data:
    print "In row {}s, Min = {}s" .format(index, min(row))
