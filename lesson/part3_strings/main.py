

# Строки в '' и "" это одно и то же
print("'string' == \"string\"", 'string' == "string")

print("He's good man", end = '\n\n')

# Неявное объединение
string = 'Hello ' 'world'
print(string)


windowsPath = 'C:\python\new_lesson'
print(windowsPath)

# Экранирование
windowsPath = 'C:\python\\new_lesson'
print(windowsPath)

# Неформатированные строки
windowsPath = r'C:\python\new_lesson'
print(windowsPath, end = '\n\n')


# Python сам разберется со слешами при переходе на другие платформы (можно везде использовать / )


string = """То что вводите,
то и получаете: \u00A9'Конфуций' """
print(string)
