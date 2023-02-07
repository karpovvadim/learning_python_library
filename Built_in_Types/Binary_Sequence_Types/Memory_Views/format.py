"""format"""
# Строка, содержащая формат (в модульном стиле struct) для каждого элемента в представлении.
# memoryview может быть создан из экспортёров со строками произвольного формата, но
# некоторые методы (например, tolist()) ограничены собственными одноэлементными форматами.

# Изменено в версии 3.3: формат 'B' теперь обрабатывается в соответствии с синтаксисом
# модуля структуры. Это означает, что memoryview(b'abc')[0] == b'abc'[0] == 97.

import array

a = array.array('l', [1, 2, 3])
x = memoryview(a)
print("x.format =", x.format)

print(memoryview(b'abc')[0] == b'abc'[0] == 97)
