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

print("\n----add(elem)----Добавляет элемент elem в множество-----")

elem = 'owrty'
s.add(elem)
print(s)

print("\n--remove(elem)--Удаляет элемент elem из множества. Вызывает KeyError,"
      " если elem не содержится в множестве")
elem = 'owrty'
s.remove(elem)
print(s)

print("\n---discard(elem)--Удаляет элемент elem из множества, если он присутствует--")
elem = 'a'
s.discard(elem)   # отказаться
print(s)

print("\n---pop()--Удаляет и возвращает произвольный элемент из множества."
      " Вызывает KeyError, если множество пусто.")
el = s.pop()
print(el, s)

print("\n---clear()--Убирает все элементы из множества----")
s.clear()
print(s)

# Обратите внимание, что неоператорные версии методов update(), intersection_update(),
# difference_update() и symmetric_difference_update() принимают любую итерацию в качестве
# аргумента.
#
# Обратите внимание, что аргумент elem для методов __contains__(), remove() и discard() может
# быть набором. Чтобы облегчить поиск эквивалентного Frozenset, из elem создаётся временный.
