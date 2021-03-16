import csv


def read_data() -> object: #read data
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    data = read_data()
    sales = []
    expenditures = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale) #collect sales
    for row in data:
        expenditure = int(row['expenditure'])
        expenditures.append(expenditure) #collect expenditures

    total_s = sum(sales)
    total_ex = sum(expenditures)
    print(f'total sales:{total_s}') #output total sales
    print(f'total expenditures: {total_ex})

run()
