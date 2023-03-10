""" int.bit_length()"""
# Возвращает количество битов, необходимых для представления целого числа в двоичном
# формате, исключая знак и ведущие нули:

n = -37
print(bin(n))
print(n.bit_length())

# Точнее, если x отличен от нуля, то x.bit_length() — это уникальное положительное целое
# число k, такое что 2**(k-1) <= abs(x) < 2**k. Эквивалентно, когда abs(x) достаточно
# мало, чтобы иметь правильно округленный логарифм, тогда k = 1 + int(log(abs(x), 2)).
# Если x равно нулю, то x.bit_length() возвращает 0.
#     Эквивалентно:


def bit_length(self):
    s = bin(self)        # двоичное представление:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b')  # удалить ведущие нули и знак минус
    return len(s)        # len('100101') --> 6


print(bit_length(n))
#     Добавлено в версии 3.1.
