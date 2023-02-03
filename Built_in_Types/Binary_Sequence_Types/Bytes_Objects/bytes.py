"""class bytes([source[, encoding[, errors]]])"""
print("-------class bytes()----Без аргументов---------------------")
b = bytes()
print(b)

try:
    c = bytes(None)
    print(c)
except TypeError:
    print("TypeError: cannot convert 'NoneType' object to bytes")

print("\n-----class bytes(source, encoding)----С исходной строкой----------------")
# Любая строка, предоставленная без кодировки, вызовет TypeError.
# Точно так же попытка изменить объект bytes также приведет к тому же исключению,
# поскольку он неизменен по своей природе.

try:
    a = bytes('Hello from AskPython')
except TypeError:
    print('We need to specify string encoding always!')

b = bytes('Hello from AskPython', 'UTF-8')
print(type(b), b)

try:
    b[0] = 10
except TypeError:
    print('byte objects are immutable!')

print("\n-----class bytes(source)----С исходным целым числом-----------")
# Целое число инициализирует это количество объектов байтовых элементов в массиве.

a = bytes(10)
print(type(a), a)

print("\n-----class bytes(source)----С итеративным источником-----------")
# Это инициализирует массив с len(iterable) числом элементов, каждый из которых имеет
# значение, равное соответствующему элементу на итерируемом. Доступ к значениям байтовых
# массивов можно получить с помощью обычной итерации, но их нельзя изменить,
# поскольку они неизменяемы.

a = bytes([1, 2, 100])
print(type(a), a)
a = bytes([50, 100, 76])
print(type(a), a)
print("lenght =", len(a))

# Чтобы получить доступ к значениям массива байтов, мы можем перебрать его!
for byte_obj in a:
    print(byte_obj)

# Все остальное на Iterable приведет к TypeError
try:
    a = bytes([1, 2, 3, 'Hi'])
except TypeError:
    print("TypeError: Объект 'str' не может быть интерпретирован как целое число")

print("\n-----class bytes(source)----С кодировкой----------------")

print(bytes("bytes", encoding="utf-8"))   #  utf-8 кодирование только кирилицы
print(bytes("Байты", encoding="utf-8"))
print("bytes".encode("utf-8"))
print("Байты".encode("utf-8"))

