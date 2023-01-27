# Чтобы прояснить приведенные выше правила (см. README.md), вот пример кода Python,
# эквивалентного встроенному хешу, для вычисления хеша рационального числа float или
# complex

import math
import sys


def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.
        (Вычислить хэш рационального числа m/n)
    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).
        (Предполагается, что m и n — целые числа, где n положительно.
     Эквивалентно hash(fractions.Fraction(m, n))).
    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    # Удалите общие делители P. (Необязательно, если m и n уже взаимно просты.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so pow(n, P-2, P) gives
        # the inverse of n modulo P.
        # (Маленькая теорема Ферма: pow(n, P-1, P) равен 1, поэтому pow(n, P-2, P)
        # возвращает значение, обратное n по модулю P.)
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value


def hash_float(x):
    """Compute the hash of a float x.
        (Вычислить хэш числа с плавающей запятой x)
    """

    if math.isnan(x):
        return object.__hash__(x)
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())


def hash_complex(z):
    """Compute the hash of a complex number z.
        (Вычислите хэш комплексного числа z)
    """

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    # сделать подписанное сокращение по модулю 2 ** sys.hash_info.width
    M = 2 ** (sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value


print("\nhash_fraction(4, 3) =", hash_fraction(4, 3))
print("\nhash_float(1.23) =", hash_float(1.25))
print("\nhash_complex(complex(1.5, 1)) =", hash_complex(complex(1.5, 1)))

