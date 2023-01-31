

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
