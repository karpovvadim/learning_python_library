"""
class set([iterable])
class frozenset([iterable])
"""
# Возвращает новый объект set или frozenset, элементы которого взяты из iterable.
# Элементы множества должны быть хэшируемы. Для представления множества множеств внутренние
# множества должны быть объектами frozenset. Если iterable не указана, возвращается
# новое пустое множество.
print("\n-------Множества можно создавать несколькими способами:--------------------")
s1 = {'jack', 'sjoerd'}
print(type(s1), s1)

s2 = {c for c in 'abracadabra' if c not in 'abc'}
print(type(s2), s2)

fs = frozenset({'asdf'})
print(type(fs), fs)

l = ['a', 'b', 'foo']
print(set(), set('foobar'), set(l), frozenset(l))

# Экземпляры set и frozenset предоставляют следующие операции:
print("\n-----количество элементов s-----------------")
print(len(s2))

print("\n-------in, not in--------------------------------")
other = set('foobar')
s = 'o'
print(s in other)
print(s not in other)
s = {'q', 'd', 'e'}

print("\n----s.isdisjoint(other)------------------------------")
# Возвращает True, если у множества нет общих элементов с other. Множества не пересекаются
# тогда и только тогда, когда их пересечение — пустое множество.
print(other.isdisjoint(s))  # непересекающийся
s = {'a', 'o'}

print("\n-----x.issubset(other)----------------------------------")
print(s.issubset(other))  # x является подмножеством s

print('\n--Проверить, каждый ли элемент в множестве состоит из other.---')
print(s <= other)
print('\n---Проверить, является ли множество правильным подмножеством other, '
      'то есть set <= other and set != other.')
print(s < other)

print("\n------x.issuperset(other)-----------------------")
print(s.issuperset(other))

print("\n-----Проверить, есть ли в множестве все other элементы----------")
print(s >= other)
print("\n---Проверить, является ли множество подходящим надмножеством other,"
      " то есть set >= other and set != other.")
print(s > other)

print("\n-------union(*others)-------------------------------------------")
s = {'a', 'o', 'w', 'q'}
print(s.union(other))  # объединение
print("\n---Возвращает новое множество с элементами из множества и всеми остальными---")
print(s | other)

print("\n---intersection(*others)-------------------------------------")
print(s.intersection(other))  # пересечение
print("\n-------Возвращает новое множество с элементами, общими для множества и"
      " всех остальных")
print(s & other)

print("\n------ difference(*others)------------------------------------")
print(s.difference(other))
print("\n----Возвращает новое множество с элементами в множестве, которых нет в других")
print(s - other)

print("\n---symmetric_difference(other)--------------------------")
print(s.symmetric_difference(other))  # симметричная разница
print("\n---Возвращает новое множество с элементами либо в множестве, либо в other,"
      " но не с обоими.")
print(s ^ other)

print("\n---copy()--Возвращает неглубокую копию множества.-------------")
print(s.copy())

