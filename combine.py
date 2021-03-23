import csv
import matplotlib.pyplot as plt
import seaborn as sns


data = []
with open('salesv2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

sales = []
for row in data:
    sale = int(row['sales'])
    sales.append(sale) #collect sales

expenditures = []
for row in data:
    expenditure = int(row['expenditure'])
    expenditures.append(expenditure) #collect expenditures

months = []
for row in data:
    month = (row['month_date'])
    months.append(month) #collect months

def graphing():
    x=months
    y=sales
    ax=sns.stripplot(x,y);
    ax.set(xlabel='Months', ylabel='Sales')
    plt.title('Graph')
    plt.show()

total_s = sum(sales)
total_ex = sum(expenditures)
print(f'Total sales: £{total_s}')

with open('names.csv', 'w+') as csvfile: #output data into new spreasheet
    csvfile.write(f'total sales:{total_s} \n total expenditures: {total_ex}')

data2= []
def read_data() -> object: #read different data file

    with open('sales2.csv', 'r') as sales2_csv:
        spreadsheet = csv.DictReader(sales2_csv)
        for row in spreadsheet:
            data2.append(row)
    return data2

max_sale=max(sales)
min_sale=min(sales)
avg_sale= round(sum(sales) / len(sales),2)
print(f'Average Sales: £{avg_sale}')
max_sale_row={}
def search(sales):
    for x in data:
        if int(x['sales']) == int(sales):
            max_sale_row.update(x)

search(max_sale)
#print(max_sale_row)
max_sale_yr = max_sale_row['year']
max_sale_mon = max_sale_row['month']
print(f'Maximum sales: £{max_sale} \n Month with Max Sales:{max_sale_mon} \n Year with Max Sales: {max_sale_yr}')

min_sale_row={}
def search(sales):
    for x in data:
        if int(x['sales']) == int(sales):
            min_sale_row.update(x)

search(min_sale)

#print(min_sale_row)
min_sale_yr = min_sale_row['year']
min_sale_mon = min_sale_row['month']
print(f'Minimum sales: £{min_sale} \n Month with Min Sales: {min_sale_mon} \n Year with Min Sales: {min_sale_yr}')

for x in range(len(sales)):
    try:
        a= sales[x]
        b= sales[x+1]
        monthlychange = round((((b - a) / b) * 100),2)
        print(f'Monthly change from month {x+1} to {x+2}:{monthlychange} %')
    except IndexError:
        continue

#print(max_sale)
#print(min_sale)
read_data()
#print(data2)
graphing()

