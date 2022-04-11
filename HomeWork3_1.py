# Написать функцию, переводящую числительные,
# с английского на русский.

def num_translate(values):
    numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    return numbers.get(values)


print(num_translate('zero'))
print(num_translate('one'))
print(num_translate('two'))
print(num_translate('twenty'))


