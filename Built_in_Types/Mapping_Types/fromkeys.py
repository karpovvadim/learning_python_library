""" classmethod fromkeys(iterable[, value])"""
# Создать новый словарь с ключами от iterable и значениями, установленными в value.

# fromkeys() — это метод класса, который возвращает новый словарь. value по умолчанию None.
# Все значения относятся только к одному экземпляру, поэтому обычно не имеет смысла
# использовать value в качестве изменяемого объекта, такого как пустой список. Чтобы получить
# различные значения, используйте вместо этого словарное включение.
print("\n------Как создать словарь из последовательности ключей---")
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys)
print(vowels)

print("\n----со значением----------------------------------------")
# vowels keys  (гласные ключи)
keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)

print("\n---Создать словарь из списка изменяемых объектов--------")
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]
vowels = dict.fromkeys(keys, value)
print(vowels)
# обновление значения
value.append(2)
print(vowels)

# Если value является изменяемым значением (значение, которое может быть изменено),
# например, вызов, словарем и т. д., при использовании изменяемого элемента объекта по
# запросу также обновляется. Это связано с тем, что каждому конкретному элементу выпадает
# ссылка на один и тот же объект (указывает на один и тот же объект в памяти). Чтобы избежать
# этой проблемы, мы используем понимание словаря.
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]
vowels = {key: list(value) for key in keys}
# you can also use { key : value[:] for key in keys }
print(vowels)
# updating the value
value.append(2)
print(vowels)

# Здесь для каждого ключа в ключах создается и назначается новый список из значения.
# По сути, значение не присваивается элементу, но из него создается новый список, который
# затем присваивается каждому элементу в словаре.
