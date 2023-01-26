"""int.bit_count()"""
# Возвращает количество единиц в двоичном представлении абсолютного значения целого
# числа. Это также известно как подсчет населения. Пример:

n = 111
print(bin(n))
print("n.bit_count() =", n.bit_count())
print("(-n).bit_count() =", (-n).bit_count())

#     Эквивалентно:


def bit_count(self):
    return bin(self).count("1")


print("\n", bit_count(n))
#     Добавлено в версии 3.10.
