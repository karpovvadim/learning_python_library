            String Methods
            Строковые методы

Строки реализуют все общие операции над последовательностью, вместе с дополнительными методами,
рассмотренными далее.

 class str(object=b'', encoding='utf-8', errors='strict')
 str.capitalize()                 Первый символом - заглавная буква, остальные строчные.
 str.casefold()    Преобразование в нижний регистр и удаления всех регистровых различий.
 str.center(width[, fillchar])     Возврат по центру
 str.count(sub[, start[, end]])    Количество непересекающихся вхождений подстроки sub
 str.encode(encoding='utf-8', errors='strict')    Кодирует строку в bytes, по умолчанию — «utf-8»
 str.endswith(suffix[, start[, end]])  Возвращает True, если строка заканчивается указанным суффиксом
 str.expandtabs(tabsize=8)             Cимволы табуляции заменены одним или несколькими пробелами
 str.find(sub[, start[, end]])         Возвращает наименьший индекс в строке
 str.format(*args, **kwargs)       Содержит поля замены, разделённые фигурными скобками {}.
 str.format_map(mapping)           Cоздает новый словарь во время вызова метода
 str.index(sub[, start[, end]])  Возвращает номер первого вхождения или вызывает ValueError
 str.isalnum()                   Состоит ли строка из цифр или букв
 str.isalpha()                   Состоит ли строка из букв
 str.isascii()                   True, если строка пуста или все символы ASCII
 str.isdecimal()                 Состоит ли строка из десятичных символов
 str.isdigit()                   Состоит ли строка из цифр
 str.isidentifier()              True, если строка допустимый идентификатор
 str.islower()   	             Состоит ли строка из символов в нижнем регистре
 str.isnumeric()                 True, если все символы цифры 
 str.isprintable()  True, если все символы в строке доступны для печати или строка пуста
 str.isspace()      True, если в строке есть только пробелы и есть хотя бы один символ
 str.istitle()      Начинаются ли слова в строке с заглавной буквы.
 str.isupper()                   Состоит ли строка из символов в верхнем регистре
 str.join(iterable)      Возвращает строку, которая в итерации соединиться c разделителем
 str.ljust(width[, fillchar])  Возвращает строку, выровненную по левому краю [заполнить]
 str.lower()                   все символы преобразованы в нижний регистр.
 str.lstrip([chars])           копия строки с удалёнными ведущими символами [символы]
 static str.maketrans(x[, y[, z]])  возвращает таблицу перевода, для str.translate().
 str.partition(sep)
 str.removeprefix(prefix, /)
 str.removesuffix(suffix, /)
 str.replace(old, new[, count])
 str.rfind(sub[, start[, end]])      Возвращает самый высокий индекс в строке
 str.rindex(sub[, start[, end]])
 str.rjust(width[, fillchar])        Возвращает строку, выровненную по правому краю
 str.rpartition(sep)
 str.rsplit(sep=None, maxsplit=- 1)
 str.rstrip([chars])
 str.split(sep=None, maxsplit=- 1)
 str.splitlines(keepends=False)
 str.startswith(prefix[, start[, end]])
 str.strip([chars])
 str.swapcase()
 str.title()
 str.translate(table)
 str.upper()
 str.zfill(width)

Строки также поддерживают два стиля форматирования строк. Первый обеспечивает большую степень
гибкости и настройки (см. str.format(), Синтаксис строки формата и Пользовательское 
форматирование строк), а второй основан на C-стиле форматирования printf, обрабатывающий 
более узкий диапазон типов и его немного сложнее правильно использовать, но часто быстрее для
тех случаев, с которыми он может справиться (Форматирование строк в стиле printf).

Раздел Службы по обработке текста стандартной библиотеки охватывает ряд других модулей, 
которые предоставляют различные утилиты, связанные с текстом (включая поддержку регулярных 
выражений в модуле re).
