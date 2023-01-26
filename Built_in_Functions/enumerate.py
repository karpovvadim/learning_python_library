"""enumerate(iterable, start=0)"""
# Возвращает перечисляемый объект. iterable должен быть последовательностью, итератором
# или другим объектом, поддерживающим итерацию. Метод __next__() итератора, возвращаемый
# enumerate(),возвращает кортеж, содержащий счетчик (от начала, который по умолчанию равен 0)
# и значения, полученные в результате итерации по итерируемому объекту.
print("------Пример-----------------------------------------------")
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))

print("-----------Equivalent to:  (Эквивалентно)------------------")
def enumeraties(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

e = enumeraties(seasons, start=0)
print(e)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
# enumerate() принимает два параметра:
# 1. iterable — последовательность, итератор или объекты, поддерживающие итерацию
# 2. start (необязательно) — enumerate() начинает отсчет с этого числа. Если start опущен,
# 0 принимается за начало.
# Метод enumerate() в Python добавляет счетчик к итерации и возвращает его.
# Возвращаемый объект — это перечисляемый объект.
# Вы можете преобразовать перечисляемые объекты в список и кортеж, используя методы list()
# и tuple() соответственно.
print("---0----Как enumerate() работает в Python?------------------")
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumeraties(grocery, 10)
print(list(enumerateGrocery))
print("---1----Цикл по объекту Enumerate--------------------------")
for item in enumeraties(grocery):
    print("item: ", item)
    print("type(item)", type(item))
print('\n')
for count, item in enumeraties(grocery, 1):
    print("count, item: ", count, item)
    print("type(count): ", type(count))
    print("type(item): ", type(item))

""" class range(start, stop, step=1)"""
