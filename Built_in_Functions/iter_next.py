""" iter(object, sentinel)"""  # часовой (необязательно)
# Возвратите объект итератора. Первый аргумент интерпретируется очень по-разному в зависимости
# от наличия второго аргумента. Без второго аргумента object должен быть объектом-коллекцией,
# который поддерживает итерируемый протокол (метод __iter__()) или должен поддерживать протокол
# последовательности (метод __getitem__() с целочисленными аргументами, начинающимися с 0).
# Если он не поддерживает ни один из этих протоколов, возникает TypeError. Если задан второй
# аргумент, sentinel, то объект должен быть вызываемым объектом. Итератор, созданный в этом
# случае, будет вызывать объект без аргументов для каждого вызова его метода __next__(); если
# возвращаемое значение равно sentinel, StopIteration будет поднят, в противном случае будет
# возвращено значение.
# Одним из полезных применений второй формы iter() является создание блочного считывателя.
# Например, чтение блоков фиксированной ширины из двоичного файла базы данных до тех пор,
# пока не будет достигнут конец файла:
"""
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
"""
print("----0----Возвращаемое значение из iter()--------------------")
# Функция возвращает объект-итератор для данного объекта.
# Если определяемый пользователем объект не реализует __iter __() и __next __() или
# __getitem() __, возникает исключение TypeError.
# Если также указан параметр дозорного, iter() возвращает итератор до тех пор, пока знак
# дозорного не будет найден.
# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter))    # 'a'
print(next(vowels_iter))    # 'e'
print(next(vowels_iter))    # 'i'
print(next(vowels_iter))    # 'o'
print(next(vowels_iter))    # 'u'
print("----1---- Для настраиваемых объектов-------------------------")
class PrintNumber:
    def __init__(self, maximum):
        self.max = maximum

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num

    # __call__ = __next__

print_num = PrintNumber(3)
print_num_iter = iter(print_num)
# for i in print_num_iter:
#     print(i)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3
# print(next(print_num_iter))  # raises StopIteration
print("----2----С параметром--------------------------------")


class DoubleIt:
    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__    # вызывается метод __next__


my_iter = iter(DoubleIt(), 64)

for x in my_iter:
    print(x)

# Здесь мы реализовали настраиваемый итерируемый объект без условия StopIteration.
# Однако мы можем использовать метод iter() с параметром sentinel, чтобы остановить итерацию.
# Если значение, возвращаемое из __next __(), равно sentinel, StopIteration будет повышен, в
# противном случае будет возвращено значение. Функция next() возвращает следующий элемент из
# итератора.
""" next(iterator, default)"""
# Получите следующий элемент из итератора, вызвав его метод __next__().
# Если указано значение по умолчанию, оно возвращается, если итератор исчерпан,
# в противном случае вызывается StopIteration.
# Параметры
# iterator ‒ next() получает следующий элемент из итератора;
# по умолчанию (необязательно) ‒ это значение возвращается, если итератор исчерпан
# (нет следующего элемента).
# Возвращаемое значение
# Функция next() возвращает следующий элемент из итератора.
# Если итератор исчерпан, он возвращает значение по умолчанию, переданное в качестве аргумента.
# Если параметр по умолчанию опущен и итератор исчерпан, возникает исключение StopIteration.
print("---3----Получить следующий предмет-----------------------------")
random = [5, 9, 'cat']
random_iterator = iter(random)
print(random_iterator)
print(next(random_iterator))
print(next(random_iterator))
print(next(random_iterator))
# print(next(random_iterator))  # This will raise Error, iterator is exhausted (исчерпан)
# Список является повторяемым, и вы можете получить его итератор из него,
# используя функцию iter() в Python.
# Мы получили ошибку из последнего оператора в приведенной выше программе, поскольку мы
# пытались получить следующий элемент, когда следующий не был доступен (итератор исчерпан).
# В таких случаях вы можете указать значение по умолчанию в качестве второго параметра.
print("----4---- Передача значения по умолчанию-------------------------")
random = [5, 9]
random_iterator = iter(random)
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))  # random_iterator is exhausted
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
# Примечание: Внутри next() вызывает метод __next __().
