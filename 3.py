from two import get_data

transactions = get_data()[2]
sorted_by_amount = transactions.sort_values(by='amount', ascending=False).head(150)
print(sorted_by_amount.head())
median = sorted_by_amount['amount'].median()
mean = sorted_by_amount['amount'].mean()
print(f'Медиана: {median}')
print(f'Среднее: {mean}')
