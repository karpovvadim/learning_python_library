"""nbytes"""

# nbytes == product(shape) * itemsize == len(m.tobytes()). Это количество места в байтах,
# которое массив будет использовать в непрерывном представлении. Это не обязательно равно
# len(m):

import array

a = array.array('i', [1, 2, 3, 4, 5])
m = memoryview(a)
print(len(m))
print(m.nbytes)
print(len(m.tobytes()))

y = m[::2]
print(len(y))
print(y.nbytes)
print(len(y.tobytes()))

print("\n----Многомерные массивы:--------------------------------")
import struct

buf = struct.pack("d" * 12, *[1.5 * x for x in range(12)])
x = memoryview(buf)
y = x.cast('d', shape=[3, 4])
print(y.tolist())
print(len(y))
print(y.nbytes)

# New in version 3.3.
