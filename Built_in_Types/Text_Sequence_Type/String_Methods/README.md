            String Methods
            Строковые методы

Строки реализуют все общие операции над последовательностью, вместе с дополнительными методами,
рассмотренными далее.

 class str(object=b'', encoding='utf-8', errors='strict')
 str.capitalize()
 str.casefold()
 str.center(width[, fillchar])
str.count(sub[, start[, end]])
str.encode(encoding='utf-8', errors='strict')
str.endswith(suffix[, start[, end]])
 str.expandtabs(tabsize=8)
 str.expandtabs(tabsize=8)
 str.format(*args, **kwargs)
str.format_map(mapping)
str.index(sub[, start[, end]])
str.isalnum()
str.isalpha()
str.isascii()
str.isdecimal()
str.isdigit()
str.isidentifier()
str.islower()
str.isnumeric()
str.isprintable()
str.isspace()
str.istitle()
 str.isupper()
 str.join(iterable)
 str.ljust(width[, fillchar])
 str.lower()
str.lstrip([chars])
static str.maketrans(x[, y[, z]])
 str.partition(sep)
str.removeprefix(prefix, /)
 str.removesuffix(suffix, /)
str.replace(old, new[, count])
 str.rfind(sub[, start[, end]])
 str.rindex(sub[, start[, end]])
 str.rjust(width[, fillchar])
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
