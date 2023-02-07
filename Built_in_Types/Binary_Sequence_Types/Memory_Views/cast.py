"""cast(format[, shape])"""
# Преобразует memoryview в новый format или shape. shape по умолчанию
# [byte_length//new_itemsize], что означает, что вид результатов будет одномерным.
# Возвращаемое значение — новое представление памяти, но сам буфер не копируется.
# Поддерживаемые преобразования: 1D -> C-смежный и C-смежный -> 1D.

# Формат назначения ограничен собственным форматом одного элемента в синтаксисе struct.
# Один из форматов должен быть байтовым («B», «b» или «c»). Длина результата в байтах
# должна быть такой же, как и исходная длина.

print("\n----Преобразование 1D/длинных в 1D/беззнаковые байты:--------")
import array

a = array.array('l', [1, 2, 3])
x = memoryview(a)
y = x.cast("B")
print("x.format =", x.format, "     y.format =", y.format)
print("x.itemsize =", x.itemsize, "   y.itemsize =", y.itemsize)
print("len(x) =", len(x), "       len(y) =", len(y))
print("x.nbytes =", x.nbytes, "    y.nbytes =", y.nbytes)

print("\n-----Преобразование 1D/беззнаковых байтов в 1D/char:----------")
b = bytearray(b'zyz')
x = memoryview(b)
try:
    x[0] = b'a'
except TypeError:
    print('TypeError: memoryview: invalid type for format "B"')

y = x.cast('c')
y[0] = b'a'
print(b)

print("\n-----Преобразование 1D/байтов в 3D/int в 1D/знаковый char:-----")

import struct

buf = struct.pack("i" * 12, *list(range(12)))
x = memoryview(buf)
y = x.cast('i', shape=[2, 2, 3])
print(y.tolist())
z = y.cast('b')
print("y.format   =", y.format, "      z.format =", z.format)
print("y.itemsize =", y.itemsize, "    z.itemsize =", z.itemsize)
print("len(y)     =", len(y), "        len(z) =", len(z))
print("y.nbytes   =", y.nbytes, "     z.nbytes =", z.nbytes)

print("\n-----Преобразование 1D/unsigned long в 2D/unsigned long:---------")
# Преобразование 1D/ беззнаковый длинный в 2D/беззнаковое длинное:
buf = struct.pack("L" * 6, *list(range(6)))
x = memoryview(buf)
y = x.cast('L', shape=[2, 3])
print(len(y))
print(y.nbytes)
print(y.tolist())

# Добавлено в версии 3.3.
# Изменено в версии 3.5: Исходный формат больше не ограничивается при преобразовании
# в байтовое представление.
