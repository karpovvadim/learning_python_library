"""
bytes.title()
bytearray.title()
"""
# Возвращает версию двоичной последовательности с заглавными буквами, в которой слова
# начинаются с символа ASCII в верхнем регистре, а остальные символы в нижнем регистре.
# Байтовые значения без регистра остаются неизменными.
print(b'Hello world'.title())

# Строчные символы ASCII — это байтовые значения в последовательности
# b'abcdefghijklmnopqrstuvwxyz'. Символы ASCII в верхнем регистре — это байтовые значения
# в последовательности b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. Все остальные байтовые значения не
# регистровы.
# Алгоритм использует простое независимое от языка определение слова как группы
# последовательных букв. Определение работает во многих контекстах, но это означает, что
# апострофы в сокращениях и притяжательных формах образуют границы слов, что может быть
# нежелательным результатом:
print(b"they're bill's friends from the UK".title())

# Обход апострофов можно создать с помощью регулярных выражений:
import re
def titlecase(s):
    return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0:1].upper() +
                             mo.group(0)[1:].lower(),
                  s)
print(titlecase(b"they're bill's friends."))

#     Примечание
# Версия bytearray метода не работает на месте — он всегда производит новый объект,
# даже если не было изменений.
