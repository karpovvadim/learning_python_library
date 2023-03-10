#          Other Built-in Types
#          Другие встроенные типы

Интерпретатор поддерживает несколько других типов объектов. Большинство из них поддерживают
только одну или две операции.

#Modules (Модули)

Единственная специальная операция над модулем — это доступ к атрибуту: m.name, где m — это
модуль, а name — доступ к имени, определенному в таблице символов m. Атрибуты модуля могут
быть присвоены. (Обратите внимание, что оператор import, строго говоря, не является операцией
над объектом модуля; import foo не требует существования объекта модуля с именем foo, скорее
для него требуется (внешнее) определение для модуля с именем foo где-то.)

Особый атрибут каждого модуля — __dict__. Это словарь, содержащий таблицу символов модуля.
Изменение этого словаря фактически изменит таблицу символов модуля, но прямое присвоение
атрибута __dict__ невозможно (вы можете написать m.__dict__['a'] = 1, который определяет
m.a как 1, но вы не можете написать m.__dict__ = {}). Не рекомендуется напрямую изменять__dict__.

Модули, встроенные в интерпретатор, записываются так: <module 'sys' (built-in)>. При загрузке
из файла они записываются как <module 'os' from '/usr/local/lib/pythonX.Y/os.pyc'>.

# Classes and Class Instances (Классы и экземпляры классов)

См. Объекты, значения и типы и Определения класса.

# Functions (Функции)

Функциональные объекты создаются определениями функций. Единственная операция над
функциональным объектом — это вызвать его: func(argument-list).
На самом деле существует два вида функциональных объектов: встроенные функции и
пользовательские функции. Оба поддерживают одну и ту же операцию (для вызова функции), но
реализация разная, следовательно, разные типы объектов.
См. Определения функции для получения дополнительной информации.

# Methods (Методы)

Методы — это функции, которые вызываются с использованием записи атрибутов. Есть две
разновидности: встроенные методы (например, append() в списках) и методы экземпляра класса.
Встроенные методы описаны с типами, которые их поддерживают.
Если вы обращаетесь к методу (функции, определенной в пространстве имён класса) через
экземпляр, вы получаете специальный объект: объект связанный метод (также называемый метод
экземпляра). При вызове он добавит аргумент self в список аргументов. У связанных методов
есть два специальных атрибута, доступных только для чтения: m.__self__ — это объект, с
которым работает метод, и m.__func__ — это функция, реализующая метод. Вызов
m(arg-1, arg-2, ..., arg-n) полностью эквивалентен вызову на
m.__func__(m.__self__, arg-1, arg-2, ..., arg-n).
Как и объекты функций, связанные объекты методов поддерживают получение произвольных
атрибутов. Однако, поскольку атрибуты метода фактически хранятся в базовом объекте функции
(meth.__func__), установка атрибутов метода для связанных методов запрещена. Попытка
установить атрибут в методе приводит к возникновению AttributeError. Чтобы установить
атрибут метода, вам необходимо явно установить его для базового объекта функции:

>>> class C:
...     def method(self):
...         pass
...
>>> c = C()
>>> c.method.whoami = 'меня зовут метод'  # не могу установить метод
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'method' object has no attribute 'whoami'
>>> c.method.__func__.whoami = 'меня зовут метод'
>>> c.method.whoami
'меня зовут метод'

См. Стандартная иерархия типов для получения дополнительной информации.

# Code Objects (Объекты кода)

Объекты кода используются реализацией для представления «псевдо- скомпилированного»
исполняемого кода Python, такого как тело функции. Они отличаются от объектов функций,
потому что не содержат ссылки на их глобальную среду выполнения. Объекты кода возвращаются
встроенной функцией compile() и могут быть извлечены из объектов функции с помощью их
атрибута __code__. См. также модуль code.
Кодовый объект может быть выполнен или вычислен путём передачи его (вместо исходной строки)
встроенным функциям exec() или eval().
См. Стандартная иерархия типов для получения дополнительной информации.

# Type Objects (Объекты типа)

Объекты типа представляют различные типы объектов. Доступ к типу объекта осуществляется
встроенной функцией type(). Специальных операций над типами нет. Стандартный модуль types
определяет имена для всех стандартных встроенных типов.
Типы записываются так: <class 'int'>.

# The Null Object (Нулевой объект)

Объект возвращается функциями, которые явно не возвращают значение. Не поддерживает никаких
специальных операций. Существует ровно один нулевой объект с именем None (встроенное имя).
type(None)() производит такой же синглтон.
Он записывается как None.

# The Ellipsis Object (Объект многоточия)

Объект обычно используется для нарезки (см. Нарезки). Не поддерживает никаких специальных
операций. Существует ровно один объект с многоточием с именем Ellipsis (встроенное имя).
type(Ellipsis)() производит синглтон Ellipsis.
Он записывается как Ellipsis или ....

# The NotImplemented Object (Не реализованный объект)

Объект возвращается из сравнений и бинарных операций, когда их просят работать с типами,
которые они не поддерживают. См. Сравнения для получения дополнительной информации.
Есть ровно один объект NotImplemented. type(NotImplemented)() создаёт экземпляр синглетон.
Он записывается как NotImplemented.

# Boolean Values (Логические значения)

Логические значения — это два постоянных объекта False и True. Они используются для
представления значений истинности (хотя другие значения также могут считаться ложными или
истинными). В числовом контексте (например, при использовании в качестве аргумента
арифметического оператора) они ведут себя как целые числа 0 и 1 соответственно. Встроенная
функция bool() может использоваться для преобразования любого значения в логическое значение,
если это значение может быть интерпретировано как значение истинности
(см. раздел Проверка истинности выше).
Они записываются как False и True соответственно.

# Internal Objects (Внутренние объекты)

Для получения этой информации см. Иерархия стандартных типов. Он описывает объекты кадра
стека, объекты трассировки и объекты среза.