"""class bytearray([source[, encoding[, errors]]])"""
# Для объектов bytearray нет специального синтаксиса литералов, вместо этого они всегда
# создаются путём вызова конструктора:
# Создание пустого экземпляра:
b = bytearray()
print("\n", b)
# Создание экземпляра с заполнением нулями заданной длины:
arr = bytearray(5)
print(type(arr), arr)
# Из итерации целых чисел:
b = bytearray(range(20))
print("\n", b)
# Копирование существующих двоичных данных через буферный протокол:
b = bytearray(b'Hi!')
print("\n", b)

print("\n-------class bytearray(source, encoding)-------------------")
string = "Байты"
arr = bytearray(string, 'utf-8')  # string with encoding 'utf-8'
print(arr)

string = "Python is interesting."
arr = bytearray(string, 'utf-8')  # utf-8 кодирование только кирилицы
print(arr)

print("\n-------class bytearray(source)------------------------------")

string = b"Python is interesting."
arr = bytearray(string)
print(type(arr), arr)

try:
    c = bytearray(None)
    print(c)
except TypeError:
    print("TypeError: cannot convert 'NoneType' object to bytearray")

print("\n-----class bytearray(source)----С итеративным источником-----------")
a = bytearray([1, 2, 100])
print(type(a), a)
a = bytearray([50, 100, 76])
print(type(a), a)
print("lenght =", len(a))

# Чтобы получить доступ к значениям массива байтов, мы можем перебрать его!
for byte_obj in a:
    print(byte_obj)

# Все остальное на Iterable приведет к TypeError
try:
    a = bytearray([1, 2, 3, 'Hi'])
except TypeError:
    print("TypeError: Объект 'str' не может быть интерпретирован как целое число")


