# Создайте новый словарь. Объект dict — это класс словаря.
# См. документацию по этому классу в разделе dict и Mapping Types — dict.
# Для других контейнеров см. встроенные классы списков, наборов и кортежей,
# а также модуль коллекций.
# Конструктор dict() создает словарь в Python. Различные формы конструкторов dict():
"""class dict(**kwarg) """
"""class dict(mapping, **kwarg)"""
"""class dict(iterable, **kwarg) """
# Примечание:
# ** kwarg позволяет вам принимать произвольное количество аргументов ключевого слова.
# Аргумент ключевого слова — это аргумент, которому предшествует идентификатор
# (например, name =). Следовательно, аргумент ключевого слова в форме kwarg = value
# передается в конструктор dict() для создания словарей.
# dict() не возвращает никакого значения (не возвращает None).
print("--Cоздать словарь, используя только аргументы ключевого слова--")
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))
empty = dict()
print('empty =', empty)
print(type(empty))
print("----Создание словаря с использованием Iterable---------------")
# keyword argument is not passed (аргумент ключевого слова не передается)
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =', numbers1)
# keyword argument is also passed (аргумент ключевого слова также передается)
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =', numbers2)

# zip() creates an iterable in Python 3 (zip() создает итерируемый объект в Python 3)
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =', numbers3)
