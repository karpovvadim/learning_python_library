"""
bytes.translate(table, /, delete=b'')
bytearray.translate(table, /, delete=b'')
"""
# Возвращает копию байтов или объекта байтового массива, где все байты, встречающиеся в
# необязательном аргументе delete удалены, а оставшиеся байты были сопоставлены с данной
# таблицей преобразования, которая должна быть байтовым объектом длиной 256.

# Вы можете использовать метод bytes.maketrans() для создания таблицы преобразования.

# Установка аргумента table в None таблицы преобразования, приведёт только к удалению
# символов:
print("-----table = None------------------------------------------")
c = b'read this short text'
b = bytearray(c)
print(b)
print(b'read this short text'.translate(None, b'aeiou'))
print(b.translate(None, b'aeiou'))

print("\n-----c table---------------------------------------------")
firstString = b"abc"
secondString = b"ghi"
string = b"abcdef"
print("Original string:", string)
translation = string.maketrans(firstString, secondString)

print("translation: ", translation)
thirdString = b"ab"
print("Translated string:", string.translate(translation, delete=thirdString))
# в string = b"abcdef" убрали a и b; c заменили на i; >>> idef

print("\n-----bytearray.translate(table, /, delete=b'')--------------------")
firstString = b"abc"
print(firstString)
secondString = b"ghi"
string = b"abcdef"
string_arr = bytearray(string)
print("Original string:", string_arr)
translation = string_arr.maketrans(firstString, secondString)

print("translation: ", translation)
thirdString = b"ab"
print("Translated string:", string_arr.translate(translation, delete=thirdString))
# в string_arr = bytearray(b'abcdef') убрали a и b; c заменили на i; >>> idef

