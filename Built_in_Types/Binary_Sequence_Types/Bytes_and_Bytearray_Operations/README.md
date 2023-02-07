            Bytes and Bytearray Operations
            Байты и операции с байтовыми массивами

И байты, и объекты байтового массива поддерживают общие операции над последовательностью.
Они взаимодействуют не только с однотипными операндами, но и с любым байтоподобным
объектом. Благодаря такой гибкости их можно свободно смешивать в операциях, не вызывая
ошибок. Однако тип возвращаемого результата может зависеть от порядка операндов.

Примечание
Методы для байтов и объектов bytearray не принимают строки в качестве своих аргументов,
так же как методы для строк не принимают байты в качестве своих аргументов.
Например, вам нужно написать:

a = "abc"
b = a.replace("a", "f")

а также:

a = b"abc"
b = a.replace(b"a", b"f")

Некоторые операции с байтами и байтовыми массивами предполагают использование двоичных
форматов, совместимых с ASCII, и, следовательно, их следует избегать при работе с
произвольными двоичными данными. Эти ограничения описаны ниже.

Примечание

Использование этих операций на основе ASCII для управления двоичными данными, которые не
хранятся в формате на основе ASCII, может привести к повреждению данных.

Следующие методы для байтов и объектов байтовых массивов могут использоваться с
произвольными двоичными данными.

bytes.count(sub[, start[, end]])   Количество непересекающихся вхождений подстроки sub
bytearray.count(sub[, start[, end]])        Аналогично str

bytes.removeprefix(prefix, /)      удалить prefix. возвращает string[len(prefix):]
bytearray.removeprefix(prefix, /)           Аналогично str

bytes.removesuffix(suffix, /)      удалить суффикс. вернуть string[:-len(suffix)]
bytearray.removesuffix(suffix, /)           Аналогично str

bytes.decode(encoding='utf-8', errors='strict')     преобразует байты в строку Python.
bytearray.decode(encoding='utf-8', errors='strict') обратная ф-ция str.encode()

bytes.endswith(suffix[, start[, end]])  Возвращает True, если строка заканчивается suffix
bytearray.endswith(suffix[, start[, end]])  Аналогично str

bytes.find(sub[, start[, end]])         Возвращает наименьший индекс в строке
bytearray.find(sub[, start[, end]])         Аналогично str

bytes.index(sub[, start[, end]]) Возвращает номер первого вхождения или вызывает ValueError
bytearray.index(sub[, start[, end]])        Аналогично str

bytes.join(iterable) Возвращает конкатенацию строк, которая в итерации соединиться c разделителем
bytearray.join(iterable)                    Аналогично str

static bytes.maketrans(from, to)     возвращает таблицу перевода, для bytes.translate()
static bytearray.maketrans(from, to) from и to должны быть байтоподобными объектами и 
                                     содержать одинаковую длину.

bytes.partition(sep)        Возвращает до разделителя, разделитель и после разделителя
bytearray.partition(sep)                    Аналогично str

bytes.replace(old, new[, count])   заменена старой подстроки новой
bytearray.replace(old, new[, count])        Аналогично str

bytes.rfind(sub[, start[, end]])    Возвращает самый высокий индекс в строке
bytearray.rfind(sub[, start[, end]])        Аналогично str

bytes.rindex(sub[, start[, end]]) Возвращает индекс в строке. ValueError если sub не найдена
bytearray.rindex(sub[, start[, end]])       Аналогично str

bytes.rpartition(sep)       Возвращает до разделителя, разделитель и после разделителя.
bytearray.rpartition(sep)                   Аналогично str

bytes.startswith(prefix[, start[, end]]) Возвращает True, если строка начинается с prefix
bytearray.startswith(prefix[, start[, end]])    Аналогично str

bytes.translate(table, /, delete=b'') Возвращает копию байтов или объекта байтового массива,
bytearray.translate(table, /, delete=b'') где все байты=delete удалены, а оставшиеся
                                            сопоставлены с данной таблицей преобразования

У следующих методов для байтов и объектов байтовых массивов поведение по умолчанию,
предполагающее использование двоичных форматов, совместимых с ASCII, но все же могут
использоваться с произвольными двоичными данными путём передачи соответствующих аргументов.
Обратите внимание, что все методы bytearray в этом разделе не работают на месте, а вместо
этого создают новые объекты.

bytes.center(width[, fillbyte])         Возврат по центру
bytearray.center(width[, fillbyte])     Аналогично str

bytes.ljust(width[, fillbyte]) Возвращает строку, выровненную по левому краю [заполнить]
bytearray.ljust(width[, fillbyte])      Аналогично str

bytes.lstrip([chars])   копия строки с удалёнными ведущими символами [символы]
bytearray.lstrip([chars])               Аналогично str

bytes.rjust(width[, fillbyte])  Возвращает строку, выровненную по правому краю
bytearray.rjust(width[, fillbyte])      Аналогично str

bytes.rsplit(sep=None, maxsplit=- 1) распадается. Возвращает список слов в строке справа
bytearray.rsplit(sep=None, maxsplit=- 1)    Аналогично str

bytes.rstrip([chars]) Возвращает копию строки с удаленными завершающими символами
bytearray.rstrip([chars])               Аналогично str

bytes.split(sep=None, maxsplit=- 1) распадается. Возвращает список слов в строке
bytearray.split(sep=None, maxsplit=- 1)     Аналогично str

bytes.strip([chars]) распадается. Возвращает список слов в строке с удаленными символами 
bytearray.strip([chars])          в начале и в конце     Аналогично str

Следующие ниже методы для байтов и объектов байтовых массивов предполагают использование
двоичных форматов, совместимых с ASCII, и не должны применяться к произвольным двоичным
данным. Обратите внимание, что все методы bytearray в этом разделе не работают на месте,
а вместо этого создают новые объекты.

bytes.capitalize()      Первый символом - заглавная буква, остальные строчные.
bytearray.capitalize()                  Аналогично str

bytes.expandtabs(tabsize=8)   Cимволы табуляции заменены одним или несколькими пробелами
bytearray.expandtabs(tabsize=8)         Аналогично str

bytes.isalnum()         Состоит ли строка из цифр или букв
bytearray.isalnum()                     Аналогично str

bytes.isalpha()         Состоит ли строка из букв
bytearray.isalpha()                     Аналогично str

bytes.isascii()         True, если строка пуста или все символы ASCII
bytearray.isascii()                     Аналогично str

bytes.isdigit()         Состоит ли строка из цифр
bytearray.isdigit()                     Аналогично str

bytes.islower()         Состоит ли строка из символов в нижнем регистре
bytearray.islower()                     Аналогично str

bytes.isspace()     True, если в строке есть только пробелы и есть хотя бы один символ
bytearray.isspace()                     Аналогично str

bytes.istitle()     Начинаются ли слова в строке с заглавной буквы.
bytearray.istitle()                     Аналогично str

bytes.isupper()     Состоит ли строка из символов в верхнем регистре
bytearray.isupper()                     Аналогично str

bytes.lower()       все символы преобразованы в нижний регистр.
bytearray.lower()                       Аналогично str

bytes.splitlines(keepends=False) Возвращает список строк в строке, разрывая границы строк
bytearray.splitlines(keepends=False)    Аналогично str

bytes.swapcase()        Возвращает копию строки, случай обмена регистра
bytearray.swapcase()                    Аналогично str

bytes.title() Возвращает копию строки, слова начинаются с прописных букв, а остальные — строчными
bytearray.title()                       Аналогично str

bytes.upper()           Возвращает копию строки, преобразованую в верхний регистр.
bytearray.upper()                       Аналогично str

bytes.zfill(width)      Возвращает копию строки, заполненную цифрами ASCII '0'
bytearray.zfill(width)                  Аналогично str