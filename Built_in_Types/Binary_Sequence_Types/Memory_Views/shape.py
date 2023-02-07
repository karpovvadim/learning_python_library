"""shape"""

# Кортеж целых чисел длиной ndim, задающий форму памяти в виде N-мерного массива.

b = bytearray(b'zyz, abc')
x = memoryview(b)
print(x.shape)

# Изменено в версии 3.3: Пустой кортеж вместо None, когда ndim = 0.
