#!/usr/bin/env python3

# Модель присваивания едина во всем языке

a = 3
b = a
print(a == b, a is b)


b = 'spam'
print(a == b, a is b)


a = [1, 2, 3]
b = a
b.append(4)
print(a == b, a is b)


# Кеш
a = 2
b = 2
print(a is b)