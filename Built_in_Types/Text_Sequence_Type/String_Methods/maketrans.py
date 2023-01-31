"""static str.maketrans(x[, y[, z]])"""  # сделать перевод
# Этот статический метод возвращает таблицу перевода, которую можно использовать для
# str.translate().
# Если есть только один аргумент, это должен быть словарь, отображающий порядковые номера
# Unicode (целые числа) или символы (строки длины 1) в порядковые номера Unicode, строки
# (произвольной длины) или None. Символьные ключи затем будут преобразованы в порядковые.
# Если есть два аргумента, они должны быть строками одинаковой длины, и в результирующем
# словаре каждый символ в x будет сопоставлен с символом в той же позиции в y. Если есть
# третий аргумент, это должна быть строка, символы которой в результате будут сопоставлены
# с None.

print("---------static str.maketrans(x)----сделать перевод---------------")
dict_ = {"a": "123", "b": "456", "c": "789"}  # example dictionary
string = "abc"
print(string.maketrans(dict_))

print("\n---------static str.maketrans(x[, y])----сделать перевод---------------")
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))

firstString = "abc"
secondString = "defghi"
string = "abc"
# print(string.maketrans(firstString, secondString)) ValueError: the first two maketrans
# arguments must have equal length

print("\n---------static str.maketrans(x[, y[, z]])-----сделать перевод--------------")
firstString_ = "abc"
secondString_ = "def"
thirdString = 'wraf'
string_ = "def"
print(string_.maketrans(firstString_, secondString_, thirdString))
