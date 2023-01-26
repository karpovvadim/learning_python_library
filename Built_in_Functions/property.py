"""class property(fget=None, fset=None, fdel=None, doc=None)"""
# Конструкция property() возвращает атрибут свойства.
# Синтаксис:
# property(fget=None, fset=None, fdel=None, doc=None)
#             Параметры
# Свойство функции принимает четыре необязательных параметра:
# 1. fget (необязательно) ‒ функция для получения значения атрибута. По умолчанию Нет.
# 2. fset (необязательно) ‒ для установки значения атрибута. По умолчанию Нет.
# 3. fdel (необязательно) ‒ для удаления значения атрибута. По умолчанию Нет.
# 4. doc (необязательно) ‒ строка, содержащая документацию (docstring) для атрибута.
# По умолчанию Нет.
#             Возвращаемое значение из свойства
# Метод возвращает атрибут свойства из заданного средства получения, установки и удаления:
# 1. Если аргументы не указаны, конструктор возвращает базовый атрибут свойства,
# который не содержит никаких средств получения, установки или удаления.
# 2. Если doc не предоставлен, тип принимает строку документации функции получения.
print("-----Создание атрибута с помощью метода получения, установки и удаления-----")
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name:      ', self._name)
        return self._name

    def set_name(self, value):
        print('Setting name to: ' + value, "  from: ", self._name)
        self._name = value

    def del_name(self):
        print('Deleting name:', self._name)
        del self._name
    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print("p.name:  ", p.name)
p.name = 'John'
del p.name
print("Name property: ", __doc__)
# Здесь _name используется в качестве частной переменной для хранения имени Person.
# Также устанавливаем:
# метод получения get_name() для получения имени человека;
# метод установки set_name() для установки имени человека;
# метод удаления del_name() для удаления имени человека.
# Теперь мы устанавливаем новое имя атрибута свойства, вызывая метод property().
# Как показано в программе, обращение к p.name изнутри вызывает get_name() как
# getter, set_name() как setter и del_name() как deleteter через напечатанный вывод,
# присутствующий внутри методов.
# Если указано, doc будет строкой документации атрибута свойства. В противном случае
# свойство скопирует строку документации fget (если она существует). Это позволяет легко
# создавать свойства только для чтения, используя свойство() в качестве декоратора:
print("-----------Использование декоратора---------------------------------")
# Вместо использования property() в Python вы можете использовать декоратор @property()
# для назначения получателя, установщика и удалителя.
class Person_2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("I'm the 'name' property. Getting name:  ", self._name)
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to: ' + value, "from: ", self._name)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name:', self._name)
        del self._name

p_2 = Person_2('Adam')
print('The name is:', p_2.name)
p_2.name = 'John'
del p_2.name
# Здесь вместо использования property() мы использовали декоратор @property.
# Во-первых, мы указываем, что метод name() также является атрибутом Person.
# Это делается с помощью @property перед методом получения, как показано в программе.
# Затем мы используем имя атрибута, чтобы указать установщик и удалитель.
# Это делается с помощью @ name.setter для метода установки и @ name.deleter для
# метода удаления.
# Обратите внимание, мы использовали одно и то же имя метода() с разными определениями
# для определения получателя, установщика и удалителя.
# Теперь, когда мы используем p.name, он внутренне вызывает соответствующий метод
# получения, установки и удаления, как показано в распечатанном выводе,
# присутствующем внутри метода.
# Возвращенный объект свойства также имеет атрибуты fget, fset и fdel, соответствующие
# аргументам конструктора.
# Изменено в версии 3.5: строки документации объектов свойств теперь доступны для записи.
