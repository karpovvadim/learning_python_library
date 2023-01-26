"""float.as_integer_ratio()"""
# Возвращает пару целых чисел, отношение которых точно равно исходному float,
# и с положительным знаменателем.
# Вызывает OverflowError для бесконечностей и ValueError для NaN.
from decimal import Decimal

n = 0.25
print(n.as_integer_ratio())

# Никогда им не пользуйтесь Потому что:

print(0.2.as_integer_ratio())
# (3602879701896397, 18014398509481984)

# Виной всему стандарт представления дробных чисел IEEE 754, который реализует float.
# Используйте Decimal:

n = Decimal("0.2")
print(n.as_integer_ratio())
