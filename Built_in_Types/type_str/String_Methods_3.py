print("---------------str.isspace()----пробел-----------------------")
# Возвращает True, если в строке есть только пробельные символы и есть хотя бы один
# символ, в противном случае — False.
# Символ является пробелом, если в базе данных символов Unicode (см. unicodedata)
# либо его общая категория — Zs («Разделитель, пробел»),
# либо его двунаправленный класс — один из WS, B или S.
# Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'),
# "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и
# "вертикальная табуляция" ('\v'))
s = '   \t'
print(s.isspace())
s = ' a '
print(s.isspace())
s = ''
print(s.isspace())

s = '\t  \n'
if s.isspace():
    print('All whitespace characters')
else:
    print('Contains non-whitespace characters')

s = '2+2 = 4'
if s.isspace():
    print('All whitespace characters')
else:
    print('Contains non-whitespace characters.')
print("--------str.istitle()--------заглавие---------------------------")
# Верните True, если строка является строкой с заглавным регистром и содержит хотя бы
# один символ, например, символы верхнего регистра могут следовать только за
# символами без регистра, а символы нижнего регистра — только за символами в регистре.
# В противном случае верните False.
# Начинаются ли слова в строке с заглавной буквы.
print("-------str.join(iterable)-----присоединиться-----------------------")
# Возвращает строку, которая представляет собой конкатенацию строк в итерации. Ошибка
# TypeError будет вызвана, если в итерации есть какие-либо нестроковые значения, включая
# объекты байтов. Разделителем между элементами является строка, обеспечивающая этот метод.
# Сборка строки из списка с разделителем S.
# Функция принимает в качестве параметра итерацию (объекты, способные возвращать свои члены
# по одному).
# Вот некоторые из примеров итераций:
# 1. Собственные типы данных ‒ список, кортеж, строка, словарь и набор.
# 2. Файловые объекты и объекты, которые определены с помощью __iter __() или __getitem() __.
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))  # .join() with lists
numTuple = ('1', '2', '3', '4')  # .join() with tuples
print(separator.join(numTuple))
s1 = 'abc'
s2 = '123'  # .join() with str
print('s1.join(s2):', s1.join(s2))  # '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s2.join(s1):', s2.join(s1))  # 'a'+ '123'+ 'b'+ '123'+ 'b'
print("-------str.join(iterable)----с множествами-------------------------")
test = {'2', '1', '3'}
s = ', '
print(s.join(test))  # .join() with sets
test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))
print("-------str.join(iterable)----со словарями-------------------------")
test = {'mat': 1, 'that': 2}  # .join() with dictionaries
s = '->'
print(s.join(test))  # joins the keys only
# test = {1: 'mat', 2: 'that'}
# s = ', '
# print(s.join(test))    # this gives error since key isn't string
print("-----------str.ljust(width[, fillchar])------просто с лева-----------------")
# Возвращает строку, выровненную по левому краю в строке длины ширины. Заполнение
# выполняется с использованием указанного символа заполнения (по умолчанию используется
# пробел ASCII). Исходная строка возвращается, если ширина меньше или равна len(s).
print('cat'.ljust(5, '*'))  # print left justified string
print("----------str.rjust(width[, fillchar])------просто с права---------------")
# Возвращает строку, выровненную по правому краю, в строке длины ширины. Заполнение
# выполняется с использованием указанного символа заполнения (по умолчанию используется
# пробел ASCII). Исходная строка возвращается, если ширина меньше или равна len(s).
print('cat'.rjust(5, '*'))  # print right justified string
print("-------str.lstrip([chars])--------полоска с лева----------------------")
# Возвращает копию строки с удаленными ведущими символами. Аргумент chars представляет
# собой строку, определяющую набор удаляемых символов. Если он опущен или None, аргумент
# chars по умолчанию удаляет пробелы. Аргумент chars не является префиксом;
# скорее, все комбинации его значений удаляются:
random_string = '   this is good '
print(random_string.lstrip())  # Leading whitepsace are removed
print(random_string.lstrip('sti'))  # Argument doesn't contain space. No characters are removed.
print(random_string.lstrip('s thi'))
website = 'https://pythonstart.ru/'
print(website.lstrip('htps:/.'))
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
