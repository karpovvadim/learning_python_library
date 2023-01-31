"""str.isnumeric()"""   # числовой   Как использовать?
# Возвращает True, если все символы в строке являются цифрами и есть хотя бы один символ,
# в противном случае возвращает False. Числовые символы включают цифровые символы и все
# символы, которые имеют свойство числового значения Unicode, например. U+2155,
# VULGAR FRACTION ONE FIFTH (ВУЛГАРНАЯ Дробь ОДНА ПЯТАЯ_. Формально числовые символы —
# это символы со значением свойства Numeric_Type=Digit, Numeric_Type=Decimal
# или Numeric_Type=Numeric.
s = '\u00B23455'   # s = '²3455'
print(s.isnumeric())
if s.isnumeric():
    print('All characters are numeric.')
else:
    print('All characters are not numeric.')
s = '\u00BD'   # s = '½'
print(s.isnumeric())
s = 'python12'
print(s.isnumeric())