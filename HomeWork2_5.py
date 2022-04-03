# список содержащий цены на товары.
list_of_prices = [
    54.67, 39.89, 145.99,
    97.8, 289, 765.85,
    896.5, 456.21, 432.8,
    900.9, 800.5, 1000.1
]
print(id(list_of_prices))

list_of_prices.sort()

print(''.join(str(list_of_prices)))

