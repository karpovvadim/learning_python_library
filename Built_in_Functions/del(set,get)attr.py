print("---------Функция delattr()--------------------------------")
# Функция delattr() удаляет атрибут из объекта (если объект позволяет это).
# Синтаксис функции:
# delattr(object, name)
# Параметры
# delattr() в Python принимает два параметра:
# object — объект, из которого нужно удалить атрибут name.
# name — строка, которая должна быть именем атрибута, который нужно удалить из объекта.
# delattr() не возвращает никакого значения (не возвращает None).
# Он удаляет только атрибут (если объект позволяет это). Пример 1: Как работает delattr()?
class Coordinate:
    x = 10
    y = -5
    z = 20


point1 = Coordinate()

print('x = ', Coordinate.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordinate, 'y')

print('--After deleting y attribute--')
print('x = ', point1.x)
# print('y = ', point1.z)  # Raises Error
print('z = ', point1.z)
print("---------оператор del-------------------------------------")
# Пример 2: Удаление атрибута с помощью оператора del

del Coordinate.z

print('--After deleting z attribute--')
print('x = ', point1.x)

# print('z = ', point1.z)  # Raises Attribute Error
print("-------Функция setattr()----------------------------------")
# Функция setattr() устанавливает значение атрибута объекта.
# Синтаксис функции:
#                   setattr(object, name, value)
# Если вы хотите получить атрибут объекта, используйте getattr().
# Параметры
# Функция принимает три параметра:
# объект ‒ объект, атрибут которого должен быть установлен;
# name ‒ имя атрибута;
# значение ‒ значение, присвоенное атрибуту.
# Возвращаемое значение
# Метод setattr() в Python ничего не возвращает; не возвращает None.
# Пример 1: Как работает?


class Person:
    name = 'Adam'


p = Person()
print('Before modification:', p.name)
# setting name to 'John'
setattr(p, 'name', 'John')
print('After modification:', p.name)
# Пример 2: Когда атрибут не найден
# Если атрибут не найден, команда создает новый атрибут и присваивает ему значение.
# Однако это возможно только в том случае, если объект реализует метод __dict __().
print("-------Пример 2: Когда атрибут не найден---------------")


class Person:
    name = 'Adam'


p = Person()
setattr(p, 'name', 'John')   # setting attribute name to John
print('Name is:', p.name)

setattr(p, 'age', 23)  # setting an attribute not present in Person
print('Age is:', p.age)
print("----------Пример как getattr() работает в Python?--------------")
# Метод getattr() возвращает значение названного атрибута объекта.
# Если не найден, он возвращает значение по умолчанию, предоставленное функции.
# Синтаксис:
# getattr(object, name[, default])
# Вышеупомянутый синтаксис эквивалентен: object.name
# getattr() в Python принимает несколько параметров:
# объект — объект, чье значение именованного атрибута должно быть возвращено.
# name — строка, содержащая имя атрибута.
# по умолчанию (необязательно) — значение, которое возвращается, если именованный атрибут не найден.
# getattr() возвращает:
# значение названного атрибута данного объекта;
# по умолчанию, если именованный атрибут не найден;
# Исключение AttributeError, если именованный атрибут не найден и значение по умолчанию не определено.


class Person:
    age = 23
    name = "Adam"


person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
print("-------Пример 2: когда именованный атрибут не найден-----------------")
#  когда указано значение по умолчанию
print('The sex is:', getattr(person, 'sex', 'Male'))  # when default value is provided
print('The sex is:', getattr(person, 'sex'))  # when no default value is provided
