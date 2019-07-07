# list - МАССИВ указателей языка С++


obj = [1, '2', [3, 4], None]
print(len(obj))


print('2' in obj)


for item in obj:
    print(item, end = ' ')


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

firstLine = matrix[0]

# Изменяет непосредственно список
firstLine[:2] = [1, 2, 3, 4, 5]
print()
print(matrix)

# Удаляет элементы среза [0:1] - 0 элемент дале вставляет начиная с его позиции элементы справа от знака = - пустоту
# Операция удаления
firstLine[0:1] = []
print(firstLine)


firstLine.append(6) # ~ firstLine + [6] 1 - изменяет сам объект 2 - создает новый
# firstLine.extend([1, 2, 3])
