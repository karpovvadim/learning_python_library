"""suboffsets"""
# Используется внутри для массивов в стиле PIL. Значение носит исключительно информационный
# характер.

import array

a = array.array('l', [1, 2, 3])
x = memoryview(a)

print(x.suboffsets)
