""" toreadonly()"""

# Возвращает версию объекта memoryview только для чтения. Исходный объект memoryview
# не изменился.

m = memoryview(bytearray(b'abc'))
mm = m.toreadonly()
print(mm.tolist())

try:
    mm[0] = 42
except TypeError:
    print("TypeError: cannot modify read-only memory")

m[0] = 43
print(mm.tolist())

# New in version 3.8.
