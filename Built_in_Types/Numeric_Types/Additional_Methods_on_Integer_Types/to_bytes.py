"""int.to_bytes(length=1, byteorder='big', *, signed=False)"""
#               длина = 1, порядок байтов = «большой», *, подписанный =False
# Возвращает массив байтов, представляющий целое число.

print((1024).to_bytes(2, byteorder='big'))
print((1024).to_bytes(10, byteorder='big'))
print((-1024).to_bytes(10, byteorder='big', signed=True))
x = 1000
print(x.to_bytes((x.bit_length() + 7) // 8, byteorder='little'))

# Целое число представлено length байтами и по умолчанию равно 1. Вызывается OverflowError, если целое число
# не может быть представлено заданным количеством байтов.
# Аргумент byteorder определяет порядок байтов, используемый для представления целого
# числа. Если byteorder — "big", старший байт находится в начале массива байтов. Если
# byteorder — "little", старший байт находится в конце массива байтов. Чтобы запросить
# собственный порядок байтов хостсистемы, используйте sys.byteorder в качестве значения
# порядка байтов.
# Аргумент signed определяет, используется ли дополнение до двух для представления
# целого числа. Если signed — False и задано отрицательное целое число, возникает
# OverflowError. Значение по умолчанию для signed — False.
# Значения по умолчанию можно использовать для удобного преобразования целого числа
# в однобайтовый объект. Однако при использовании аргументов по умолчанию не пытайтесь
# преобразовать значение больше 255, иначе вы получите ошибку OverflowError:
n = 65
print("\n", n.to_bytes(1, byteorder="big"))

# Equivalent to:


def to_bytes(n, length=1, byteorder='big', signed=False):
    if byteorder == 'little':
        order = range(length)
    elif byteorder == 'big':
        order = reversed(range(length))
    else:
        raise ValueError("byteorder must be either 'little' or 'big'")

    return bytes((n >> i*8) & 0xff for i in order)


print("\n", to_bytes(n))

# Добавлено в версии 3.2.
# Изменено в версии 3.11: Добавлены значения аргументов по умолчанию для length и
# byteorder
