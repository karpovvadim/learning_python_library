"""str.rstrip([chars])"""   # раздевание с права
# Возвращает копию строки с удаленными завершающими символами. Аргумент chars представляет
# собой строку, определяющую набор удаляемых символов. Если он опущен или None, аргумент
# chars по умолчанию удаляет пробелы. Аргумент символов не является суффиксом; скорее,
# все комбинации его значений удаляются:

random_string = 'this is good    '
print(random_string.rstrip())  # Trailing whitepsace are removed (Завершающие пробелы удаляются)
print(random_string.rstrip('si oo'))  # Argument doesn't contain 'd'. No characters are removed.
# (Аргумент не содержит 'd'. Никакие символы не удаляются).
print(random_string.rstrip('sid o'))
website = 'pythonstart.ru/'
print(website.rstrip('u/.'))
