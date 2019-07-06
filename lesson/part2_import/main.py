# Python
import sys


# Полный импорт
import lesson.part2_import.other    # .py - required for import
print(lesson.part2_import.other.var1)

# C псевдонимом
import lesson.part2_import.other as otherModule
print(otherModule.var1)


# Копия имени var1
from lesson.part2_import.other import var1
print(var1)

# Копия всех имен верхнего уровня
from lesson.part2_import.other import *
print(var2)


# Можно перезагрузить модуль явно
import imp
imp.reload(lesson.part2_import.other)


# dir
print(dir(lesson.part2_import.other))


# Пути поиска модулей
print(sys.path)


# exec
exec("var2 = 'changed via exec'")
print(var2)
