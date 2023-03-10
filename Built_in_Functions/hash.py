# Возвращает хеш-значение объекта (если оно есть). Хэш-значения являются целыми
# числами. Они используются для быстрого сравнения ключей словаря во время поиска
# в словаре. Числовые значения, которые сравниваются равными, имеют одно и то же
# значение хеш-функции (даже если они относятся к разным типам, как в случае 1 и 1.0).
# Примечание
# Для объектов с пользовательскими методами __hash__() обратите внимание, что hash()
# усекает возвращаемое значение в зависимости от разрядности хост-компьютера.
# Подробнее см. __hash__().
# Метод hash() возвращает хеш-значение объекта, если оно есть.
# Значения хэша – это просто целые числа, которые используются для быстрого сравнения
# ключей словаря во время поиска в словаре. Внутренне метод вызывает __hash __()
# объекта, который установлен по умолчанию для любого объекта. Мы рассмотрим это позже.
# Синтаксис:
"""hash(object)"""
# Параметры
# Метод hash() в Python принимает единственный параметр:
# object – объект, хеш-значение которого должно быть возвращено (целое число, строка,
# число с плавающей запятой).
# Хэш возвращает значение объекта, если оно есть.
# Если у объекта есть собственный метод __hash __(), он обрезает возвращаемое значение
# до размера Py_ssize_t.
print("--------хэш для целого числа без изменений------------------------")
# hash for integer unchanged (хэш для целого числа без изменений)
print('Hash for 181 is:', hash(181))
print("--------хэш для десятичного числа---------------------------------")
# hash for decimal
print('Hash for 181.23 is:',hash(181.23))
print("--------хэш для строки 'Python'-----------------------------------")
# hash for string
print('Hash for Python is:', hash('Python'))
# Хеш-ункция работает только для неизменяемых объектов в виде кортежа.
print("---------Для неизменяемого объекта кортежа------------------------")
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print('The hash is:', hash(vowels))
# Как работает с настраиваемыми объектами?
# Как указано выше, функция внутренне вызывает метод __hash __(). Итак, любые объекты
# могут переопределить __hash __() для пользовательских значений хеша.
# Но для правильной реализации хеша __hash __() всегда должен возвращать целое число.
# И должны быть реализованы оба метода __eq __() и __hash __().
# Ниже приведены примеры правильного переопределения __hash __().
#             Кейсы для реализации пользовательского хэша для объектов
# __eq __()            __hash __()              Описание
# Определено        Определено       Если оставить как есть, все объекты сравниваются
# (по умолчанию)    (по умолчанию)   неравно (кроме самих себя).

# (Если изменяемый) Не следует       Реализация хешируемой коллекции требует, чтобы
# Определен         определять       хеш-значение ключа было неизменным.

# Не определен      Не следует       Если __eq __() не определен, __hash __()
#                                    определять  не должен определяться.

# Определенный      Не определен     Экземпляры классов нельзя будет использовать как
#                                    хешируемую коллекцию. __hash __() неявно установлено
#                                    значение None. Вызывает исключение TypeError при
#                                    попытке получить хэш.

# Определенный      Сохранить от     __hash__ =<ParentClass.__ hash__
#                   родителя

# Определенный      Не хочет         __hash__ = None. Вызывает исключение TypeError при
#                   хешировать       попытке получить хэш.
print("-----Для настраиваемых объектов путем переопределения __hash __()-----")
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print("1_hash(self.age): ", hash(self.age))
        print("1_hash(self.name): ", hash(self.name))

    # def __eq__(self, other):
    #     return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))

person = Person(23, 'Adam')
print("hash(person): ", hash(person))
print("hash(Person(18, 'Anna')): ", hash(Person(18, 'Anna')))
# Примечание:
# Не нужно реализовывать метод __eq __() для хэша, поскольку он создается
# по умолчанию для всех объектов.


