# Задание №3, реализовать склонение слова процент.
percent_one = 'процент'
percent_two = 'процента'
percent_three = 'процентов'

i = 0
for i in range(101):
    if (i % 10 == 0 or
            i == 11 or
            i == 12 or
            i == 13 or
            i == 14 or
            5 <= i % 10 <= 9):
        print(str(i) + percent_three)

    elif (i % 10 >= 2) and (i % 10 <= 4):
        print(str(i) + percent_two)

    elif i % 10 == 1:
        print(str(i) + percent_one)
