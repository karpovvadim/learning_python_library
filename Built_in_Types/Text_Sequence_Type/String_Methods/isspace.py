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
print("s = '   \t' =", s.isspace())

s = ' a '
print("s = '  a  ' =", s.isspace())

s = ''
print("s = '' =", s.isspace())

s = '\t  \n'
if s.isspace():
    print('All whitespace characters')  # Все пробельные символы
else:
    print('Contains non-whitespace characters')

s = '2 + 2 = 4'
if s.isspace():
    print('All whitespace characters')
else:
    print('Contains non-whitespace characters.')  # Содержит непробельные символы
