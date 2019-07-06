#!/usr/bin/env python3

var1 = 'var1 form other.py.py'
var2 = 'var2 form other.py.py'


print('Hello from other.py.py')
print('Импорт модуля приводит в конечном счете 111 к его исполнению', end='\n\n')


if __name__ == '__main__':
    print('Запущен в качестве главного модуля')
