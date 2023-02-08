f = dict({'one': 1, 'three': 3}, two=2)

print("\n---list(d)----Возвращает список всех ключей, используемых в словаре d--")
print(list(f))

print("\n---len(d)----Возвращает количество элементов в словаре d----------")
print(len(f))

print("\n--- d[key]---Возвращает элемент d с помощью ключа key. Вызывает KeyError,"
      " если ключ отсутствует в отображении.")


# Если подкласс dict определяет метод __missing__(), а key отсутствует, операция d[key]
# вызывает метод с ключом key в качестве аргумента. Затем операция d[key] возвращает или
# вызывает все, что было возвращено или вызвано вызовом __missing__(key). Никакие другие
# операции или методы не вызывают __missing__(). Если __missing__() не определен, вызывается
# KeyError. __missing__() должен быть методом; это не может быть переменной экземпляра:

class Counter(dict):
    def __missing__(self, key):
        return 0


c = Counter()
print(c['red'])
c['red'] += 1
print(c['red'])
# В приведенном выше примере показана часть реализации collections.Counter.
# Другой метод __missing__ используется collections.defaultdict.

print("\n---d[key] = value----Установить d[key] на value---------------")
f['three'] = 333
print(f['three'], f)

print("\n---del d[key]---Удалить d[key] из d. Вызывает KeyError, если key отсутствует в отображении")
del f['three']
print(f)

print("\n---key in d-----Возвращает True, если у d есть ключевой key, иначе False")
print("'one' in f >>>", 'one' in f)
print("\n---key not in d-----Эквивалентен not key in d-----------")
print("'one' not in f >>>", 'one' not in f)

print("\n---iter(d)---Возвращает итератор по ключам словаря. Это ярлык для iter(d.keys())")
d = iter(f)
print(d)

print("\n---clear()----Удалить все элементы из словаря------------")
f.clear()
print(f)

print("\n---copy()--------Возвращает неглубокую копию словаря-------")
d = dict([('two', 2), ('one', 1), ('three', 3)])
z = d.copy()
print(z)
