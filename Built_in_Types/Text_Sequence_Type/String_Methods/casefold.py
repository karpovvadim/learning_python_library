"""str.casefold()"""   # чехол
# Возвращает свернутую копию строки. Строки с регистром могут использоваться для
# безрегистрового сопоставления.
# Сворачивание регистра похоже на преобразование в нижний регистр, но более агрессивно,
# поскольку оно предназначено для удаления всех регистровых различий в строке.
# Например, немецкая строчная буква «ß» эквивалентна «ss». Поскольку это уже нижний регистр,
# функция lower() ничего не сделает с 'ß'; casefold() преобразует его в "ss".
# Алгоритм сворачивания регистров описан в разделе 3.13 стандарта Unicode.
# Новое в версии 3.3.

string = "PYTHON IS AWESOME"
print("Lowercase string:", string.casefold())
firstString = "DER Fluß"
secondString = "der Fluss"
print(secondString.casefold(), '==', firstString.casefold())

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
