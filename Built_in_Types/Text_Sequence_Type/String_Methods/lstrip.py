"""str.lstrip([chars])"""
# Возвращает копию строки с удалёнными ведущими символами. Аргумент chars — это строка,
# определяющая множество удаляемых символов. Если он пропущен или None, аргумент chars
# по умолчанию удаляет пробелы. Аргумент chars не является префиксом; скорее, удаляются
# все комбинации его значений:

print('   spacious   '.lstrip())
print('www.example.com'.lstrip('cmowz.'))
print('www.example.com'.lstrip('wz'))
