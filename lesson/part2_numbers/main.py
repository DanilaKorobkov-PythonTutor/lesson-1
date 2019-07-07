"""Числовые типы - неизменяемы"""


# Integer numbers
print('10 == 0x0A == 0b1010:', 10 == 0x0A == 0b1010, '# Types: ', type(10), type(0x0A), type(0b1010))

# Float numbers
print('1.0 == 1. == 10e-1:', 1.0 == 1. == 10e-1, '# Types: ', type(1.0), type(1.), type(10e-1))

# Complex numbers
print(1 + 1j, type(1 + 1j), end = '\n\n')


thereIsNoMaxNumber = 2 ** 500
print(thereIsNoMaxNumber, end = '\n\n')


# Приведение типов
print('type(1 + 1.1):', type(1 + 1.1), end = '\n\n')

# Python не делает неявных преобразования
# print(1 + int('1'))


# Формат
print('{0:.3f}'.format(1 / 3))
print('{:x}'.format(255), end = '\n\n') # 0x format

# /, //
print(type(1 / 2), type(1.0 / 2))
print(type(1 // 2), type(1.0 // 2), end = '\n\n')


# decimal
import decimal

one = decimal.Decimal('1.123')
two = decimal.Decimal(str(1.123))
three = decimal.Decimal(1.123)
print(one, two, three)

# decimal.getcontext().prec = 5
print(one + two)

with decimal.localcontext() as ctx:

    a = decimal.Decimal('4')
    b = decimal.Decimal('3')

    ctx.prec = 2
    print(a / b )
