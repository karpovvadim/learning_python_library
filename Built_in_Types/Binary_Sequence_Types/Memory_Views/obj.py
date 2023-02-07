""" obj"""
#     Базовый объект memoryview:

b = bytearray(b'xyz')
m = memoryview(b)
print(m.obj is b)  #    True

#     Добавлено в версии 3.3.
