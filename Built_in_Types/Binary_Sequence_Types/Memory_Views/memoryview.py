"""class memoryview(obj)"""  # Просмотры памяти

# Создать memoryview, который ссылается на obj. obj должен поддерживать протокол буфера.
# Встроенные объекты, поддерживающие протокол буфера, включают bytes и bytearray.

# У memoryview есть понятие элемента, который представляет собой атомарную единицу
# памяти, обрабатываемую исходным объектом obj. Для многих простых типов, таких как
# bytes и bytearray, элемент является однобайтным, но другие типы, такие как
# array.array, могут иметь элементы большего размера.
#
# len(view) равен длине tolist. Если view.ndim = 0, длина равна 1. Если view.ndim = 1,
# длина равна количеству элементов в представлении. Для более высоких измерений длина
# равна длине представления в виде вложенного списка. Атрибут itemsize отдаст вам
# количество байтов в одном элементе.
#
# memoryview поддерживает нарезку и индексирование для предоставления своих данных.
print('\n---Одномерная нарезка приведёт к субпредставлению:-------------')
v = memoryview(b'abcefg')
print(v[1])  # 98
print(v[-1])  # 103
print(v[1:4])  # <memory at 0x7f3ddc9f4350>
print(bytes(v[1:4]))  # b'bce'

# Если format является одним из спецификаторов собственного формата из модуля struct,
# индексирование с целым числом или кортежем целых чисел также поддерживается и возвращает
# один элемент с правильным типом. Одномерные представления памяти могут быть
# проиндексированы целым или одноцелочисленным кортежем. Многомерные представления памяти
# могут быть проиндексированы кортежами ровно ndim целых чисел, где ndim — количество
# измерений. Нульмерные просмотры памяти можно индексировать с помощью пустого кортежа.

print('\n-------пример с небайтовым форматом:----------------')

import array
a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
m = memoryview(a)
print(m[0])  # -11111111
print(m[-1])  # 44444444
print(m[::2].tolist())  # [-11111111, -33333333]

# Если базовый объект доступен для записи, memoryview поддерживает одномерное назначение
# нарезки.
print('\n-----Изменение размера не допускается:-------------------')
data = bytearray(b'abcefg')
v = memoryview(data)
print(v.readonly)  # False

v[0] = ord(b'z')
print(data)  # bytearray(b'zbcefg')

v[1:4] = b'123'
print(data)  # bytearray(b'z123fg')

try:
    v[2:3] = b'spam'
except ValueError:
    print('ValueError: memoryview assignment: lvalue and rvalue have different structures')
    # Ошибка значения: назначение представления памяти: lvalue и rvalue имеют разные структуры
v[2:6] = b'spam'
print(data)  # bytearray(b'z1spam')

# Одномерные представления памяти хешируемых (только для чтения) типов с форматами «B», «b»
# или «c» также могут быть хешированы. Хэш определяется как hash(m) == hash(m.tobytes()):
print('\n------hash()-------------------------------')
v = memoryview(b'abcefg')
print(hash(v) == hash(b'abcefg'))  # True
print(hash(v[2:4]) == hash(b'ce'))  # True
print(hash(v[::-2]) == hash(b'abcefg'[::-2]))  # True

# Изменено в версии 3.3: Одномерные представления памяти теперь можно нарезать. Одномерные
# представления памяти с форматами «B», «b» или «c» теперь хешируются.
# Изменено в версии 3.4: memoryview теперь автоматически регистрируется в
# collections.abc.Sequence
# Изменено в версии 3.5: memoryviews теперь можно индексировать с помощью кортежа целых чисел.

# У memoryview есть несколько методов:

# __eq__(exporter)
# tobytes(order='C')
# hex([sep[, bytes_per_sep]])
# tolist()
# toreadonly()
# release()
# cast(format[, shape])

# Также доступно несколько атрибутов, доступных только для чтения:
# obj
# nbytes
# readonly
#  format
# itemsize
# ndim
