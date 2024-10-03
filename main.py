# Module 3 Practice 3

def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)

# Функция с параметрами по умолчанию
print('\n1. Функция с параметрами по умолчанию\n')
print_params()
print_params(843, 'groove street', {'c': 'Скала'})
print_params(b = 25, c = [1, 2, 3])
print_params(b = 25)
print_params(c = [1, 2, 3])

# Распаковка параметров
print('\n2. Распаковка параметров\n')
values_list = [3.14, 'Пи', False]
values_dict = {'a': [8, 4, 3], 'b': 'Казань', 'c': int}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
print('\n3.Распаковка + отдельные параметры\n')
values_list_2 = [bool, {'b': 843}]
print_params(*values_list_2, 42)
