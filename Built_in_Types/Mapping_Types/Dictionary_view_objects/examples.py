dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# iteration (итерация)
n = 0
for val in values:
    n += val
print(n)

# keys and values are iterated over in the same order (insertion order)
# ключи и значения повторяются в том же порядке (порядок вставки)
print(list(keys))
print(list(values))

# view objects are dynamic and reflect dict changes
# объекты просмотра являются динамическими и отражают изменения dict
del dishes['eggs']
del dishes['sausage']
print(list(keys))

# set operations  (набор операций)
print(keys & {'eggs', 'bacon', 'salad'})
print(keys ^ {'sausage', 'juice'})

# get back a read-only proxy for the original dictionary
# вернуть прокси-сервер только для чтения для исходного словаря
print(values.mapping)
print(values.mapping['spam'])
