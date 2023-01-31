
print("-----------str.rstrip([chars])------раздевание с права--------------------")
# Возвращает копию строки с удаленными завершающими символами. Аргумент chars представляет
# собой строку, определяющую набор удаляемых символов. Если он опущен или None, аргумент
# chars по умолчанию удаляет пробелы. Аргумент символов не является суффиксом; скорее,
# все комбинации его значений удаляются:
random_string = 'this is good    '
print(random_string.rstrip())  # Trailing whitepsace are removed
print(random_string.rstrip('si oo'))  # Argument doesn't contain 'd'. No characters are removed.
print(random_string.rstrip('sid oo'))
website = 'pythonstart.ru/'
print(website.rstrip('u/.'))
print("---------str.strip([chars])-------раздевание--------------------------------")
# Возвращает копию строки с удаленными начальными и конечными символами. Аргумент chars
# представляет собой строку, определяющую набор удаляемых символов. Если он опущен или None,
# аргумент chars по умолчанию удаляет пробелы. Аргумент chars не является префиксом или
# суффиксом; скорее, все комбинации его значений удаляются:
string = '  xoxo love xoxo   '
print(string.strip())  # Leading and trailing whitespaces are removed
print(string.strip(' xoe'))  # All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip('stx'))  # Argument doesn't contain space .No characters are removed.
string = 'android is awesome'
print(string.strip('an'))
print("---------static str.maketrans(x)-----сделать перевод----------------------")
# Этот статический метод возвращает таблицу перевода, которую можно использовать для
# str.translate().
# Если есть только один аргумент, это должен быть словарь, отображающий порядковые номера
# Unicode (целые числа) или символы (строки длины 1) в порядковые номера Unicode, строки
# (произвольной длины) или None. Символьные ключи затем будут преобразованы в порядковые.
# Если есть два аргумента, они должны быть строками одинаковой длины, и в результирующем
# словаре каждый символ в x будет сопоставлен с символом в той же позиции в y. Если есть
# третий аргумент, это должна быть строка, символы которой в результате будут сопоставлены
# с None.
dict_ = {"a": "123", "b": "456", "c": "789"}  # example dictionary
string = "abc"
print(string.maketrans(dict_))
dict_ = {97: "123", 98: "456", 99: "789"}  # example dictionary
string = "abc"
print(string.maketrans(dict_))
print("---------static str.maketrans(x[, y])----сделать перевод---------------")
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))
# firstString = "abc"
# secondString = "defghi"
# string = "abc"
# print(string.maketrans(firstString, secondString)) ValueError: the first two maketrans
# arguments must have equal length
print("---------static str.maketrans(x[, y[, z]])-----сделать перевод--------------")
firstString_ = "abc"
secondString_ = "def"
thirdString = 'wraf'
string_ = "def"
print(string_.maketrans(firstString_, secondString_, thirdString))
print("--------str.translate(table)--------перевод---------------------------------")
# Возвращает копию строки, в которой каждый символ был отображен через данную таблицу
# перевода. Таблица должна быть объектом, который реализует индексацию через __getitem__(),
# обычно отображение или последовательность. При индексации по порядковому номеру Unicode
# (целому числу) объект таблицы может выполнять любое из следующих действий: возвращать
# порядковый номер Unicode или строку для сопоставления символа с одним или несколькими
# другими символами; return None, чтобы удалить символ из возвращаемой строки; или вызовите
# исключение LookupError, чтобы сопоставить символ с самим собой.
# Вы можете использовать str.maketrans() для создания карты перевода из сопоставлений
# символов в символы в различных форматах.
# См. также модуль кодеков для более гибкого подхода к пользовательским сопоставлениям символов.
firstString = "abc"
secondString = "ghi"
thirdString = "ab"
string = "abcdef"
print("Original string:", string)
translation = string.maketrans(firstString, secondString, thirdString)
print("translation: ", translation)
print("Translated string:", string.translate(translation))  # translate string
# в string = "abcdef" убрали a и b; c заменили на i; >>> idef
