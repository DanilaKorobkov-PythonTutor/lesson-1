

string = 'string'

print(len(string))
print(string + ' other')
print('str' in string)  # string.__contains__('str')
print('-' * 20)


# Строки - итерируемый объект
for char in string:
    print(char, end = '\t')


# Индексы
print('\n\n', string[0], sep = '')
print(string[-1], end = '\n')   # ~ string[len(string) - 1]

# Операция среза [0, 3)
print(string[0:3], string[:3], string[:-1], string[:], end = '\n\n')    # print(string.__getitem__(slice(0, 3)))

# Шаг
print(string[::2]) # 0, 2, 4
print(string[::-1]) # ~ string[0: len(string): -1] ~ Если смещение отрицательно то порядок границ меняется на противоположный string[len(string): 0 -1]


# Изменение строк
# string[0] = 'S'
string = 'S' + string[1:]

# string.find('n')
# string.replace('n', 'D')
# string.split()

# string.rstrip()
# string.startswith('s')
# string.endswith('g')


# Форматирование
print()
print('{0} is a {1}'.format('He', 'man'))

import sys
print('{0} is a {var.platform}'.format('He', var = sys))
print('{0} is a {dictionary[platform]}'.format('He', dictionary = {'platform': sys.platform}))

# Синтаксис
# {fielname or number!conversionflag:formatspec}
# conversionflag: r, s, a - reprs, str, ascii

# print('{0:>10} is a {1}'.format('He', 'man'))

# print('{0:.{1}f}'.format(1 / 3, 4))