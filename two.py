import pandas

def get_data():
    tr_mcc_codes = pandas.read_csv('data/tr_mcc_codes.csv', sep=';')
    tr_types = pandas.read_csv('data/tr_types.csv', sep=';')
    transactions = pandas.read_csv('data/transactions.csv', sep=',', nrows=500000)
    return tr_mcc_codes, tr_types, transactions

if __name__ == '__main__':
    tr_mcc_codes, tr_types, transactions = get_data()
    print(tr_mcc_codes.head(), '\n')
    print(tr_types.head(), '\n')
    print(transactions.head())