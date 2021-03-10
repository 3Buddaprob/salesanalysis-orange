import csv


def read_data() -> object:
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    data = read_data()
    sales = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    print(f'total sales:{total}')


#asdas

run()
