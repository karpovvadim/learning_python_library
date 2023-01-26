"""classmethod int.from_bytes(bytes, byteorder='big', *, signed=False)"""
# Возвращает целое число, представленное данным массивом байтов.

print(int.from_bytes(b'\x00\x10', byteorder='big'))
print(int.from_bytes(b'\x00\x10', byteorder='little'))
print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=True))
print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=False))
print(int.from_bytes([255, 0, 0], byteorder='big'))

# Байты аргумента должны быть либо байтоподобным объектом, либо итерируемым
# производящим байты.
# Аргумент порядка байтов определяет порядок байтов, используемый для представления
# целого числа, и по умолчанию имеет значение «большой». Если порядок байтов "большой",
# старший байт находится в начале массива байтов.
# Если порядок байтов "маленький", самый старший байт находится в конце массива байтов.
# Чтобы запросить собственный порядок байтов хост-системы, используйте sys.byteorder
# в качестве значения порядка байтов.
# Аргумент со знаком указывает, используется ли дополнение до двух для представления
# целого числа.
#
# Эквивалентно:

byte_s = b'\xfc\x00'


def from_bytes(byte_s, byteorder='big', signed=False):
    if byteorder == 'little':
        little_ordered = list(byte_s)
    elif byteorder == 'big':
        little_ordered = list(reversed(byte_s))
    else:
        raise ValueError("byteorder must be either 'little' or 'big'")

    n = sum(b << i*8 for i, b in enumerate(little_ordered))
    if signed and little_ordered and (little_ordered[-1] & 0x80):
        n -= 1 << 8*len(little_ordered)

    return n


print("\n", from_bytes(byte_s))

# Новое в версии 3.2.
# Изменено в версии 3.11: Добавлено значение аргумента по умолчанию для порядка байтов.
