# Преобразование метода в метод класса.
# Метод класса получает класс как неявный первый аргумент, точно так же, как метод экземпляра
# получает экземпляр. Чтобы объявить метод класса, используйте эту идиому:
# class C:
#     @classmethod
#     def f(cls, arg1, arg2): ...
# Форма @classmethod является декоратором функции — подробности см. в разделе
# «Определения функций». Метод класса можно вызывать либо для класса (например, C.f()),
# либо для экземпляра (например, C().f()). Экземпляр игнорируется, за исключением его класса.
# Если метод класса вызывается для производного класса, объект производного класса
# передается в качестве подразумеваемого первого аргумента.
# Методы класса отличаются от статических методов C++ или Java.
# Если вам это нужно, см. staticmethod() в этом разделе. Дополнительные сведения
# о методах класса см. в разделе Стандартная иерархия типов.
# Изменено в версии 3.9: методы класса теперь могут заключать в себе
# другие дескрипторы, такие как свойство().
# Изменено в версии 3.10: методы класса теперь наследуют атрибуты метода
# (__module__, __name__, __qualname__, __doc__ и __annotations__) и
# имеют новый атрибут __wrapped__.
# Изменено в версии 3.11: методы класса больше не могут заключать в
# себе другие дескрипторы, такие как свойство().


def regular_function(x, y):
    return x + y


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):  # убедительная проверка. self это ссылка на
            # текущий экземпляр класса, а он содержит инормацию о классе
            self.x = x
            self.y = y
        print("staticmethod_0:  ", self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    # Преобразование метода в статический метод.
    # Статический метод не получает неявный первый аргумент.
    # Чтобы объявить статический метод, используйте эту идиому:
    # class C:
    #     @staticmethod
    #     def f(arg1, arg2, ...): ...
    # Форма @staticmethod является декоратором функции — подробности см. в разделе
    # «Определения функций».
    # Статический метод можно вызвать либо для класса (например, C.f()), либо для экземпляра
    # (например, C().f()). Более того, их можно вызывать как обычные функции (например, f()).
    # Статические методы в Python аналогичны методам в Java или C++. Также см. classmethod()
    # для варианта, полезного для создания альтернативных конструкторов классов.
    # Как и все декораторы, staticmethod также можно вызывать как обычную функцию и что-то
    # делать с ее результатом. Это необходимо в некоторых случаях, когда вам нужна ссылка на
    # функцию из тела класса, и вы хотите избежать автоматического преобразования в метод
    # экземпляра. В этих случаях используйте эту идиому:
    # def regular_function():
    #     ...
    #
    # class C:
    #     method = staticmethod(regular_function)
    # Дополнительные сведения о статических методах см. в разделе Стандартная иерархия типов.
    # Изменено в версии 3.10: Статические методы теперь наследуют атрибуты метода
    # (__module__, __name__, __qualname__, __doc__ и __annotations__), имеют новый атрибут
    # __wrapped__ и теперь могут вызываться как обычные функции.

    @staticmethod
    def norm2(x, y):
        return x*x + y*y

    method = staticmethod(regular_function(5, 10))
    print("staticmethod_3", method)


v = Vector(1, 2)
print("regulamethod_0:  ", Vector.get_coord(v))  # на классе вызваем метод с экземпляром класса
print("classmethod:  ", Vector.validate(5))   # на классе вызваем метод класса с параметром, не создавая объекта
v2 = Vector(1, 200)
print("regulamethod_1:  ", Vector.get_coord(v2))  # на классе вызваем метод с экземпляром класса
v3 = Vector(10, 20)
print("regulamethod_1:  ", v3.get_coord())  #  вызваем метод у экземпляром класса
print("staticmethod_1: ", Vector.norm2(5, 6))  # на классе вызваем статический метод с экземпляром класса
print("staticmethod_2: ", v3.norm2(5, 10))  #  вызваем статический метод у экземпляром класса
