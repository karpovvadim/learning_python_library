# Аргументы представляют собой строку и необязательные глобальные и локальные переменные.
# Если указано, глобальные переменные должны быть словарем. Если предоставлено, локальные
# могут быть любыми объектами сопоставления.
# Аргумент выражения анализируется и оценивается как выражение Python (технически говоря,
# список условий) с использованием словарей globals и locals в качестве глобального и
# локального пространства имен. Если словарь globals присутствует и не содержит значения
# для ключа __builtins__, перед разбором выражения под этим ключом вставляется ссылка
# на словарь встроенных модулей. Таким образом, вы можете контролировать, какие встроенные
# функции доступны для исполняемого кода, вставляя свой собственный словарь __builtins__
# в глобальные переменные перед передачей их в eval(). Если словарь locals опущен, по
# умолчанию используется словарь globals. Если оба словаря опущены, выражение выполняется
# с глобальными и локальными переменными в среде, где вызывается eval(). Обратите внимание,
# что eval() не имеет доступа к вложенным областям (нелокальным) во внешней среде.
#
# Метод eval() анализирует выражение, переданное этому методу, и запускает выражение (код)
# Python внутри программы. Проще говоря, функция eval() запускает код Python (который
# передается в качестве аргумента) в программе.
# Синтаксис:
print("---cинтаксис: eval(expression, globals=None, locals=None)---")
print("eval('25*6')),# globals=None, locals=None) =>", eval('25*6'))  # , globals=None, locals=None))
# Функция eval() принимает три параметра:
# 1. выражение — строка анализируется и оценивается как выражение Python.
# 2. globals (необязательно) — словарь.
# 3. locals (необязательно) — объект отображения. Словарь — это стандартный и
# часто используемый тип сопоставления.
print("----Метод eval() возвращает результат, вычисленный на основе выражения.----")
x = 10
print("x=10, eval('x + 5'):  ", eval('x + 5'))

# Эту функцию также можно использовать для выполнения произвольных объектов кода
# (например, созданных с помощью compile()). В этом случае передайте объект кода вместо
# строки. Если объект кода был скомпилирован с 'exec' в качестве аргумента режима,
# возвращаемое значение eval() будет None.
# Подсказки: динамическое выполнение операторов поддерживается функцией exec(). Функции
# globals() и locals() возвращают текущий глобальный и локальный словари, соответственно,
# которые может быть полезно передать для использования функциями eval() или exec().
# Если данный источник является строкой, то начальные и конечные пробелы
# и табуляции удаляются.
# См. ast.literal_eval() для функции, которая может безопасно оценивать строки с
# выражениями, содержащими только литералы.
# Вызывает событие аудита exec с объектом кода в качестве аргумента.
# Также могут вызываться события компиляции кода.

"""
def calculatePerimeter(length):  # Perimeter of Square
    return 4 * length


def calculateArea(length):  # Area of Square
    return length * length


expression = input("Type a function: ")

for width in range(1, 5):
    if expression == 'calculatePerimeter(width)':
        print("If length is ", width, ", Perimeter = ", eval(expression))
    elif expression == 'calculateArea(width)':
        print("If length is ", width, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
"""
print("---------Предупреждения при использовании eval()---------")
# Рассмотрим ситуацию, когда вы используете систему Unix (macOS, Linux и т. Д.)
# И импортировали модуль ОС. Модуль os предоставляет переносимый способ использования
# функций операционной системы, таких как чтение или запись в файл.
# Если вы разрешаете пользователям вводить значение с помощью eval (input()),
# пользователь может вводить команды для изменения файла или даже удаления всех
# файлов с помощью команды: os.system (‘rm -rf *’).
# Если вы используете eval (input()) в своем коде, рекомендуется проверить,
# какие переменные и методы может использовать пользователь. Вы можете увидеть,
# какие переменные и методы доступны, используя метод dir().
import math
print("--------Если опущены и глобальные, и локальные параметры--------")
print("import math, eval('dir()'):", eval('dir()'))

# Передача глобальных параметров
# Параметры globals и locals (словари) используются для глобальных и локальных
# переменных соответственно. Если словарь locals опущен, по умолчанию используется
# словарь globals . Это означает, что глобальные переменные будут использоваться
# как для глобальных, так и для локальных переменных.
# Примечание. Вы можете проверить текущий глобальный и локальный словарь в Python,
# используя встроенные методы globals() и locals() соответственно.
print("---Передача пустого словаря в качестве параметра глобальных переменных---")
print("eval('dir()', {}):         ", eval('dir()', {}))
# The code will raise an exception
"""print("eval('sqrt(25)', {}):      ", eval('math.sqrt(25)', {}))"""
# Если вы передаете пустой словарь в качестве глобальных , для выражения доступны
# только __builtins__ (первый параметр eval()).
# Несмотря на то, что мы импортировали математический модуль в приведенную выше программу,
# выражение не может получить доступ к функциям, предоставляемым математическим модулем.
print("-------Обеспечение доступности определенных методов--------")
print(eval('dir()', {'sqrt': math.sqrt, 'pow': pow}))
# Здесь выражение может использовать только методы sqrt() и pow() вместе с __builtins__.
print("------Название метода можно изменить по своему желанию.------")
names = {'square_root': math.sqrt, 'power': pow}
print(eval('dir()', names))
print("-----square_root() вычисляет квадратный корень с помощью sqrt().-------")
print(eval('square_root(25)', names))  # Using square_root in Expression
# В приведенной выше программе square_root() вычисляет квадратный корень с
# помощью sqrt(). Однако попытка использовать sqrt() напрямую вызовет ошибку.
# 5 Ограничение использования встроенных модулей
# Вы можете ограничить использование __builtins__ в выражении следующим образом:
print("-------ограничение использования __builtins__------------")
print(eval('2*5', {'__builtins__': None}))
print("-----Передача как глобальных, так и локальных словарей--------")
print("a=169;  eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': math.sqrt})")
a = 169
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': math.sqrt}))
