"""class set([iterable])"""

other = set('foobar')
s = {'q', 'd', 'e', 'a', 'o'}

print("\n------update(*others)----------------------")
s.update(other)
print(s)
s = {'q', 'd', 'e', 'a', 'o'}
print("----Обновить множество, добавив элементы из всех остальных----")
print(s | other)

print("\n-----intersection_update(*others)------------------")
s = {'q', 'd', 'e', 'a', 'o'}
s.intersection_update(other)  # пересечение_обновление
print(s)
s = {'q', 'd', 'e', 'a', 'o'}
print("---Обновить множество, сохранив только элементы, найденные в нём и все остальные-")
print(s & other)

print("\n---difference_update(*others)-------------------------------")
s = {'q', 'd', 'e', 'a', 'o'}
s.difference_update(other)  # разница_обновление
print(s)
s = {'q', 'd', 'e', 'a', 'o'}
print("---Обновляет множество, удалив элементы, найденные в других--------")
print(s - other)

print("\n-----symmetric_difference_update(other)-------------------------")
s = {'q', 'd', 'e', 'a', 'o'}
s.symmetric_difference_update(other)  # симметричная разница_обновление
print(s)
s = {'q', 'd', 'e', 'a', 'o'}
print("---Обновляет множество, сохранив только элементы, найденные в любом множестве,"
      "но не в обоих")
print(s ^ other)
