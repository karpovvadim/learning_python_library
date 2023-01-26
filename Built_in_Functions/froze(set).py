"""class frozenset(iterable=set())"""
# Возвращает новый замороженный объект набора, возможно, с элементами, взятыми из
# итерации. Frozenset — это встроенный класс. См. FrozenSet и Set Types — set,
# FrozenSet для документации по этому классу.
""" class set(iterable)"""
# Возвращает новый объект набора, необязательно с элементами, взятыми из итерируемого.
# set — это встроенный класс. См. документацию по этому классу в разделе set и
# Set Types — set, frostset.
# Встроенная функция set() создает набор в Python.
# Синтаксис: set(iterable)
# set() принимает единственный необязательный параметр:
# iterable (необязательно) — последовательность (строка, кортеж и т. д.) или коллекция
# (набор, словарь и т. д.) или объект-итератор, который нужно преобразовать в набор.
# set() возвращает:
# 1. пустой набор, если параметры не переданы.
# 2. набор, построенный из заданного итеративного параметра.
print("-------Создание наборов из строки, кортежа, списка и диапазона-------")
# empty set
print(set())
# from string
print("from string 'Python': ", set('Python'))
# from tuple
print("from tuple: ", set(('a', 'e', 'i', 'o', 'u')))
# from list
print("from list: ", set(['a', 'e', 'i', 'o', 'u']))
# from range
print("from range: ", set(range(5)))
print("---- Создание наборов из другого набора, словаря и frozenset набора-----")
# from set
print("from set: ", set({'a', 'e', 'i', 'o', 'u'}))
# from dictionary
print("from dictionary: ", set({'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}))
# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print("from frozen set: ", set(frozen_set))
print("-----Создание set() для настраиваемого итерируемого объекта-------")


class PrintNumber:
    def __init__(self, max):  # Shadows built-in name 'max' (Встроенное имя теней 'max')
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num


# print_num is an iterable (print_num является итерируемым)
# print_num = PrintNumber(5)
print("set(PrintNumber(5)): ", set(PrintNumber(5)))
# Функция frozenset() возвращает неизменяемый объект frozenset, инициализированный
# элементами из данного итеративного объекта. frozenset набор — это просто неизменная
# версия объекта набора Python. Хотя элементы набора можно изменить в любое время,
# элементы замороженного набора остаются неизменными после создания. Благодаря этому
# такие наборы можно использовать как ключи в Словаре или как элементы другого набора.
# Но, как и набор, он не упорядочен (элементы могут быть установлены по любому индексу).
# Синтаксис frozenset(): frozenset([iterable])
# Функция frozenset() принимает единственный параметр:
# iterable (Необязательно) — итерируемый объект, который содержит элементы для
# инициализации Frozenset. Iterable может быть установлен, словарь, кортеж и т. д.
# Функция возвращает неизменяемый Frozenset, инициализированный элементами из
# заданного итеративного объекта.
# Если параметры не переданы, возвращается пустой Frozenset.
print("----------------Пример 1-------------------------")
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:  ', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable  (замороженные наборы неизменны)
"""fSet.add('v')"""
# Когда вы используете словарь как итерацию для замороженного набора, для создания
# набора нужны только ключи словаря.
print("-----------Пример 2: frozenset() для словаря--------------")
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:  ', fSet)
print("------Операции-------------------------------------------")
# Как и обычные наборы, frozenset может также выполнять различные операции, такие
# как копирование, различие, пересечение, симметричное_различие и объединение.

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print("C = A.copy():      ", C)
# union
print("A.union(B):        ", A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})
# intersection
print("A.intersection(B): ", A.intersection(B))  # Output: frozenset({3, 4})
# difference
print("A.difference(B):   ", A.difference(B))  # Output: frozenset({1, 2})
# symmetric_difference (симметричная_разница)
print("A.symmetric_difference(B): ", A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})
# Точно так же доступны другие методы набора, такие как isdisjoint,
# issubset и Issuperset.
# Frozensets initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])
# isdisjoint() method (непересекающийся)
print("A.isdisjoint(C): ", A.isdisjoint(C))  # Output: True
# issubset() method (является подмножеством)
print("C.issubset(B): ", C.issubset(B))  # Output: True
# issuperset() method (является надмножеством)
print("B.issuperset(C): ", B.issuperset(C))  # Output: True

