"""all(iterable)"""
# Возвратите True, если все элементы итерации истинны (или если итерация пуста).
# Эквивалентно:
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

"""any(iterable)"""
# Верните True, если какой-либо элемент итерации имеет значение true. Если
# итерируемый объект пуст, верните False.
# Эквивалентно:
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

class ABC:
    def __init__(self, x=10):
        self.x = x

    def __bool__(self):
        if self.x == 10:
            return False
        else:
            return True


my_list = [ABC(), ABC(3)]
print(type(ABC()))
print(ABC())
print(all(my_list))
print(any(my_list))
print(type(all(my_list)))

list_2 = []
print(all(list_2))
print(any(list_2))

