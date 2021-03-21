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

with open('names.csv', 'w+') as csvfile:
    csvfile.write(f'total sales:{total_s} \n total expenditures: {total_ex}')

data2= []
def read_data() -> object: #read data

    with open('sales2.csv', 'r') as sales2_csv:
        spreadsheet = csv.DictReader(sales2_csv)
        for row in spreadsheet:
            data2.append(row)
    return data2

max_sale=max(sales)
min_sale=min(sales)

# for row in data:
#     print ("In row %s, Max = %s" % (index, max(row))
#
# for row in data:
#     print ("In row %s, Min = %s" % (index, min(row))

max_sale_row={}
def search(sales):
    for x in data:
        if int(x['sales']) == int(sales):
            max_sale_row.update(x)

search(max_sale)
print(max_sale_row)
max_sale_yr = max_sale_row['year']
max_sale_mon = max_sale_row['month']
print(max_sale_mon,max_sale_yr)

for x in data:
    a=x['sales']
    b=x + 1['sales']
    monthlychange = ((b-a)/b)*100
    print(monthlychange)

print(max_sale)
print(min_sale)
read_data()
print(data2)
graphing()

