# dict - таблица указателей языка С++

# Сохраняет порядок начиная с 3.7 для всех реализаций интерпретатора
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print(d)

len(d) # кол-во ключей: 4

# Доступ
d.get('banana', None)


# Все ключи строки
d2 = dict(banana = 3, apple = 4) # **d
print(d2)

dict.fromkeys(['a', 'b'], 0)
