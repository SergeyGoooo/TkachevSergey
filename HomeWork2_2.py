# Задание №2 необходимо
# обработать список.
temp = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха',
        'была', '+5', 'градусов']

print(temp)

temp.remove('5')
temp.remove('+5')

temp.insert(1, '05')
temp.insert(8, '+05')

temp.insert(1, '""')
temp.insert(3, '""')
temp.insert(5, '""')
temp.insert(7, '""')
temp.insert(12, '""')
temp.insert(14, '""')
print(temp)

print(' '.join(temp))