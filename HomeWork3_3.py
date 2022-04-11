# Функция принимающая в качестве аргументов
# имена сотрудников, и возвращающая словарь.

def thesaurus(*args):
    dict_name = {}

    for name in args:

        if dict_name.get(name[0]):
            dict_name[name[0]].append(name)
        else:
            dict_name[name[0]] = [name]

    return dict_name

print(thesaurus('Миша', 'Маша', 'Коля'))


