print("-----Экранированные последовательности-----------------------------")
S = "s\np\ta\nbbb"
print(S)
print("-----Неформатированные строки (подавляют экранирование)-------------")
S2 = r"s\np\ta\nbbb"
print(S2)
S1 = r"C:\temp\new"
print(S1)
print("-------Строка байтов------------------------------------------------")
S = b"byte"
print(S)
print("-------Конкатенация (сложение строк)-------------------------------")
print(S1 + S2)
print("-------Повторение строки-------------------------------------------")
print(S1 * 3)
print("-----------S.index(str, [start],[end])-----------------------------")
# Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
print("-----------S.rindex(str, [start],[end])-----------------------------")
# Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
print("--------str.isalnum()-----------буква-цифра--------------------------")
# Возвращает True, если все символы в строке буквенно-цифровые и есть хотя бы один символ,
# в противном случае возвращает False. Символ c является буквенно-цифровым, если одно из
# следующих значений возвращает True: c.isalpha(), c.isdecimal(), c.isdigit() или
# c.isnumeric().     	Состоит ли строка из цифр или букв
name = "M234onica"
print(name.isalnum())
name = "M3onica Gell22er "  # contains whitespace
print(name.isalnum())
name = "Mo3nicaGell22er"
print(name.isalnum())
name = "133"
print(name.isalnum())
print("---------str.isalpha()-------буква------------------------------------")
# Возвращает True, если все символы в строке являются буквенными и есть хотя бы один
# символ, в противном случае возвращает False. Алфавитные символы — это символы,
# определенные в базе данных символов Unicode как «буква», т. е. те, у которых свойство
# общей категории является одним из «Lm», «Lt», «Lu», «Ll» или «Lo». Обратите внимание,
# что это отличается от свойства «Алфавитный», определенного в стандарте Unicode.
#           Состоит ли строка из букв
name = "Monica"
print(name.isalpha())
name = "Monica Geller"  # contains whitespace
print(name.isalpha())
name = "Mo3nicaGell22er"  # contains number
print(name.isalpha())
print("----------str.isdecimal()--------десятичный-----------------------------")
# Возвращает True, если все символы в строке являются десятичными символами и есть хотя бы
# один символ, в противном случае возвращает False. Десятичные символы — это те, которые
# можно использовать для формирования чисел по основанию 10, например. U + 0660,
# АРАБСКАЯ ИНДИКАТОРНАЯ ЦИФРА НОЛЬ. Формально десятичный символ — это символ общей
# категории Unicode «Nd».      Состоит ли строка из десятичных символов
print("----------str.isdigit()--------цифра-----------------------------------")
# Возвращает True, если все символы в строке являются цифрами и есть хотя бы один символ,
# в противном случае — False. Цифры включают десятичные символы и цифры, требующие
# специальной обработки, например цифры надстрочного индекса совместимости. Это касается
# цифр, которые нельзя использовать для образования чисел с основанием 10, таких как
# числа Харости. Формально цифра — это символ со значением свойства Numeric_Type=Digit
# или Numeric_Type=Decimal.      Состоит ли строка из цифр
print("---------str.isidentifier()-------идентификатор-----------------------")
# Верните True, если строка является допустимым идентификатором в соответствии с
# определением языка, разделом «Идентификаторы и ключевые слова».
# Вызовите keyword.iskeyword(), чтобы проверить, является ли строка s зарезервированным
# идентификатором, таким как def и class.
from keyword import iskeyword

print('hello'.isidentifier(), iskeyword('hello'))  # (True, False)
print('def'.isidentifier(), iskeyword('def'))  # (True, True)
print('root33'.isidentifier(), iskeyword('root33'))
print('Python'.isidentifier())
print('22Python'.isidentifier())
print(''.isidentifier())
print("------str.islower()---нижний-------Как использовать в программе?-------")
# Возвращает True, если все символы [4] в строке в нижнем регистре и есть хотя бы один
# символ в регистре, в противном случае — False.
# [4] - Символы в регистре — это те, общее свойство категории которых является одним из
# «Lu» (буква, верхний регистр), «Ll» (буква, нижний регистр) или «Lt» (буква, заглавный).
#        	Состоит ли строка из символов в нижнем регистре
s = 'this is good'
if s.islower():
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')

s = 'this is Good'
if s.islower():
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')
print("-----str.isupper()---верхний-----Как в программе используется?---------")
# Возвращает True, если все символы [4] в строке в верхнем регистре и есть хотя бы один
# символ в регистре, в противном случае — False.
#               	Состоит ли строка из символов в верхнем регистре
string = "this should be uppercase!"
print(string.upper())
string = "Th!s Sh0uLd B3 uPp3rCas3!"  # string with numbers
print(string.upper())
firstString = "python is awesome!"
secondString = "PyThOn Is AwEsOmE!"
if firstString.upper() == secondString.upper():
    print("The strings are same.")
else:
    print("The strings are not same.")
print("-----str.isnumeric()----числовой----------Как использовать?----------")
# Возвращает True, если все символы в строке являются цифрами и есть хотя бы один символ,
# в противном случае возвращает False. Числовые символы включают цифровые символы и все
# символы, которые имеют свойство числового значения Unicode, например. U+2155,
# VULGAR FRACTION ONE FIFTH (ВУЛГАРНАЯ Дробь ОДНА ПЯТАЯ_. Формально числовые символы —
# это символы со значением свойства Numeric_Type=Digit, Numeric_Type=Decimal
# или Numeric_Type=Numeric.
s = '\u00B23455'   # s = '²3455'
if s.isnumeric():
    print('All characters are numeric.')
else:
    print('All characters are not numeric.')
s = '\u00BD'   # s = '½'
print(s.isnumeric())
s = 'python12'
print(s.isnumeric())
print("----str.isprintable()----для печати-------Как использовать?--------------")
# Возвращает True, если все символы в строке доступны для печати или строка пуста,
# в противном случае — False. Непечатаемые символы — это символы, определенные в базе
# данных символов Unicode как «Другие» или «Разделители», за исключением пробела
# ASCII (0x20), который считается пригодным для печати. (Обратите внимание, что печатные
# символы в этом контексте — это те символы, которые не следует экранировать при вызове
# repr() для строки. Это не имеет отношения к обработке строк, записанных в sys.stdout
# или sys.stderr.)
s = 'Space is a printable?'
print(s, s.isprintable())
s = '\nNew Line is printable?'
print(s, s.isprintable())
s = ''
print('\nEmpty string printable?', s.isprintable())
# written using ASCII
# chr(27) is escape character
# char(97) is letter 'a'
s = chr(27) + chr(97)
if s.isprintable():
    print('Printable')
else:
    print('Not Printable')
s = '2+2 = 4'
if s.isprintable():
    print('Printable')
else:
    print('Not Printable')