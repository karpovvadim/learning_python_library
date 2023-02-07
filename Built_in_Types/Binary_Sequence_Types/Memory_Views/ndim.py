"""ndim"""

# Целое число, указывающее, сколько измерений многомерного массива представляет память.

import array

a = array.array('l', [1, 2, 3])
x = memoryview(a)
print(x.ndim)

b = bytearray(b'zyz')
x = memoryview(b)
print(x.ndim)
