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

bytes.count(sub[, start[, end]])
bytearray.count(sub[, start[, end]])

bytes.removeprefix(prefix, /)
bytearray.removeprefix(prefix, /)

bytes.removesuffix(suffix, /)
bytearray.removesuffix(suffix, /)

bytes.decode(encoding='utf-8', errors='strict')
bytearray.decode(encoding='utf-8', errors='strict')

bytes.endswith(suffix[, start[, end]])
bytearray.endswith(suffix[, start[, end]])

bytes.find(sub[, start[, end]])
bytearray.find(sub[, start[, end]])

bytes.index(sub[, start[, end]])
bytearray.index(sub[, start[, end]])

bytes.join(iterable)
bytearray.join(iterable)

static bytes.maketrans(from, to)
static bytearray.maketrans(from, to)

bytes.partition(sep)
bytearray.partition(sep)

bytes.replace(old, new[, count])
bytearray.replace(old, new[, count])

bytes.rfind(sub[, start[, end]])
bytearray.rfind(sub[, start[, end]])

bytes.rindex(sub[, start[, end]])
bytearray.rindex(sub[, start[, end]])

bytes.rpartition(sep)
bytearray.rpartition(sep)

bytes.startswith(prefix[, start[, end]])
bytearray.startswith(prefix[, start[, end]])

bytes.translate(table, /, delete=b'')
bytearray.translate(table, /, delete=b'')

У следующих методов для байтов и объектов байтовых массивов поведение по умолчанию,
предполагающее использование двоичных форматов, совместимых с ASCII, но все же могут
использоваться с произвольными двоичными данными путём передачи соответствующих аргументов.
Обратите внимание, что все методы bytearray в этом разделе не работают на месте, а вместо
этого создают новые объекты.

bytes.center(width[, fillbyte])
bytearray.center(width[, fillbyte])

bytes.ljust(width[, fillbyte])
bytearray.ljust(width[, fillbyte])

bytes.lstrip([chars])
bytearray.lstrip([chars])

bytes.rjust(width[, fillbyte])
bytearray.rjust(width[, fillbyte])

bytes.rsplit(sep=None, maxsplit=- 1)
bytearray.rsplit(sep=None, maxsplit=- 1)

bytes.rstrip([chars])
bytearray.rstrip([chars])

bytes.split(sep=None, maxsplit=- 1)
bytearray.split(sep=None, maxsplit=- 1)

bytes.strip([chars])
bytearray.strip([chars])

Следующие ниже методы для байтов и объектов байтовых массивов предполагают использование
двоичных форматов, совместимых с ASCII, и не должны применяться к произвольным двоичным
данным. Обратите внимание, что все методы bytearray в этом разделе не работают на месте,
а вместо этого создают новые объекты.

bytes.capitalize()
bytearray.capitalize()

bytes.expandtabs(tabsize=8)
bytearray.expandtabs(tabsize=8)

bytes.isalnum()
bytearray.isalnum()

bytes.isalpha()
bytearray.isalpha()

bytes.isascii()
bytearray.isascii()

bytes.isdigit()
bytearray.isdigit()

bytes.islower()
bytearray.islower()

bytes.isspace()
bytearray.isspace()

bytes.istitle()
bytearray.istitle()

bytes.isupper()
bytearray.isupper()

bytes.lower()
bytearray.lower()

bytes.splitlines(keepends=False)
bytearray.splitlines(keepends=False)

bytes.swapcase()
bytearray.swapcase()

bytes.title()
bytearray.title()

bytes.upper()
bytearray.upper()

bytes.zfill(width)
bytearray.zfill(width)