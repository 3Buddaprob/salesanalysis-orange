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

graphing()
total_s = sum(sales)
total_ex = sum(expenditures)

print(f'total sales:{total_s}') #output total sales
print(f'total expenditures: {total_ex}') #output total expenditures
