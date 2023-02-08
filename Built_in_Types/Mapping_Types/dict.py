"""
class dict(**kwargs)
class dict(mapping, **kwargs)   # соответствие, отображение
class dict(iterable, **kwargs)  # повторяемый
"""

print("\n---Словари можно создавать несколькими способами:----------")
print({'jack': 4098, 'sjoerd': 4127}, "\n", {4098: 'jack', 4127: 'sjoerd'})
print({}, '\n', {x: x ** 2 for x in range(10)})
print(dict(), "\n", dict([('foo', 100), ('bar', 200)]), "\n", dict(foo=100, bar=200))

# все следующие примеры возвращают словарь, равный {"one": 1, "two": 2, "three": 3}:
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print('\na == b == c == d == e == f >>>', a == b == c == d == e == f)

# Словари сравниваются как равные тогда и только тогда, когда они имеют одинаковые пары
# (key, value) (независимо от порядка). Сравнение порядков («<», «<=», «> =», «>») вызывает
# TypeError.

# Словари сохраняют порядок вставки. Обратите внимание, что обновление ключа не влияет на
# порядок. Ключи, добавленные после удаления, вставляются в конце.
d = {"one": 1, "two": 2, "three": 3, "four": 4}

print('\n', d)
print(list(d))
print(list(d.values()))
d["one"] = 42
print(d)
del d["two"]
d["two"] = None
print(d)

# Изменено в версии 3.7: Порядок словаря гарантированно будет порядком вставки. Такое
# поведение было деталью реализации CPython из версии 3.6.
# Словари и представления словарей обратимы.
d = {"one": 1, "two": 2, "three": 3, "four": 4}
print('\n', d)
print(list(reversed(d)))
print(list(reversed(d.values())))
print(list(reversed(d.items())))

# Изменено в версии 3.8: Словари теперь обратимы.
# См.также
# types.MappingProxyType можно использовать для создания представления dict только для
# чтения.
