"""isinstance(object, classinfo)"""
# Возвратите True, если аргумент объекта является экземпляром аргумента classinfo или его
# (прямого, косвенного или виртуального) подкласса. Если объект не является объектом данного
# типа, функция всегда возвращает False. Если classinfo является кортежем объектов типа
# (или рекурсивно, другими такими кортежами) или типом объединения нескольких типов, верните True,
# если объект является экземпляром любого из типов. Если classinfo не является типом или кортежем
# типов и таких кортежей, возникает исключение TypeError. TypeError не может быть вызван для
# недопустимого типа, если предыдущая проверка прошла успешно.
# Изменено в версии 3.10: classinfo может быть Union Type.
print("-----isinstance-------------------------------------------")
numbers = [1, 2, 3]
result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)
result = isinstance(numbers, dict)
print(numbers, 'instance of dict?', result)
result = isinstance(numbers, (dict, list))
print(numbers, 'instance of dict or list?', result)
number = 5
result = isinstance(number, list)
print(number, 'instance of list?', result)
result = isinstance(number, int)
print(number, 'instance of int?', result)
class Foo:
    a = 5

fooInstance = Foo()
print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))
print("-----issubclass-------------------------------------------")
"""issubclass(class, classinfo,)"""
# Возвратите True, если класс является подклассом (прямым, косвенным или виртуальным) classinfo.
# Класс считается подклассом самого себя. classinfo может быть кортежем объектов класса
# (или рекурсивно, другими подобными кортежами) или Union Type, и в этом случае возвращайте
# True, если class является подклассом какой-либо записи в classinfo. В любом другом случае
# возникает исключение TypeError.
# Изменено в версии 3.10: classinfo может быть Union Type.
class Polygon:
    def __init__(polygonType):
        print('1 Polygon is a ', polygonType)


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')


print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))
print("2", Polygon.__init__(5))
print("3", Triangle.__init__(self=10))
