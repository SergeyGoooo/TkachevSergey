# Задание №1, вывод информации о промежутке времени,
# от его продолжительности в секундах.
duration = int(input('Введите кол-во секунд: '))

days = duration // 60 // 60 // 24
hour = duration // 3600
minutes = duration % 3600 // 60
seconds = duration % 60

print('до минуты:',
      seconds, 'сек')

print('до часа:',
      minutes, 'мин',
      seconds, 'сек')

print('до суток:',
      hour, 'час',
      minutes, 'мин',
      seconds, 'сек')

print('во всех остальных случаях:',
      days, 'дн',
      hour, 'час',
      minutes, 'мин',
      seconds, 'сек')