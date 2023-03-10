""" min(iterable, /, *, default, key=None)
    min(arg1, arg2, /, *args, key=None)"""
# Возвращает наименьший элемент в итерируемом объекте или наименьший из двух или более аргументов.
# Если указан один позиционный аргумент, он должен быть итерируемым. Возвращается наименьший
# элемент в итерации. Если указаны два или более позиционных аргумента, возвращается наименьший
# из позиционных аргументов.
# Есть два необязательных аргумента, состоящих только из ключевых слов. Ключевой аргумент задает
# функцию упорядочения с одним аргументом, подобную той, что используется для list.sort().
# Аргумент по умолчанию указывает объект, который нужно вернуть, если предоставленный
# итерируемый объект пуст. Если итерируемый объект пуст и значение по умолчанию не указано,
# возникает ошибка ValueError.
# Если несколько элементов минимальны, функция возвращает первый встреченный. Это согласуется
# с другими инструментами сохранения стабильности сортировки, такими как sorted(iterable,
# key=keyfunc)[0] и heapq.nsmalest(1, iterable, key=keyfunc).
# Новое в версии 3.4: аргумент по умолчанию, состоящий только из ключевых слов.
# Изменено в версии 3.8: Ключ может быть None.
"""min(iterable, *iterables, key, default)"""
# Параметры
# 1. iterable ‒ итерируемый объект, такой как список, кортеж, набор, словарь и т. д.;
# 2. * iterables (необязательно) ‒ любое количество итераций, может быть более одного;
# 3. key (необязательно) ‒ ключевая функция, в которую передаются итерации, и выполняется
# сравнение на основе ее возвращаемого значения;
# 4. default (необязательно) ‒ значение по умолчанию, если данная итерация пуста.
print("----1: Как получить наименьший элемент в списке?---------------------")
number = [3, 2, 8, 5, 10, 6]
smallest_number = min(number)
print("The smallest number is:", smallest_number)
# Если элементы в итеративном элементе являются строками, возвращается наименьший
# элемент (упорядоченный в алфавитном порядке).
print("----2: Наименьшая строка в списке--------------------------------")
languages = ["Python", "C Programming", "Java", "JavaScript", "A"]
smallest_string = min(languages)
print("The smallest string is:", smallest_string)
print("----3: На примере в словарях-------------------------------------")
# В случае словарей команда возвращает наименьший ключ. Давайте воспользуемся ключевым
# параметром, чтобы найти ключ словаря с наименьшим значением.
square = {2: 4, 3: 9, -5: 25, -2: 4}
print("The smallest key:", min(square))  # -5
# the key whose value is the smallest (ключ, значение которого наименьшее)
key2 = min(square, key=lambda k: square[k])
print("The key with the smallest value:", key2, type(key2))  # -2 Ключ с наименьшим значением
# getting the smallest value ( получение наименьшего значения)
print("The smallest value:", square[key2])  # 4 Наименьшее значение
# Во второй функции мы передали лямбда-функцию ключевому параметру.
# Функция возвращает значения словарей. На основе значений (а не ключей словаря)
# вычисляется ключ, имеющий минимальное значение.
# Несколько заметок:
# Если мы передаем пустой итератор, возникает исключение ValueError. Чтобы этого избежать,
# мы можем передать параметр по умолчанию.
# Если мы передаем более одного итератора, возвращается наименьший элемент из данных итераторов.
# Без итерации
# Чтобы найти наименьший элемент между двумя или более параметрами, мы можем использовать этот
# синтаксис: min(arg1, arg2, *args, key)
"""min(arg1, arg2, *args, key)"""
# Параметры
# арг1 ‒ объект, могут быть числами, строками и т. д.;
# арг2 ‒ объект, могут быть числами, строками и т. д.;
# * args (необязательно) ‒ любое количество объектов;
# key (необязательно) ‒ ключевая функция, в которую передается каждый аргумент, и сравнение
# выполняется на основе его возвращаемого значения.
# По сути, функция min() может найти наименьший элемент между двумя или более объектами.
print("-----4---Как найти минимум среди заданных чисел в Python?--------")
result = min(4, -5, 23, 5)
print("The minimum number is:", result)
# Если вам нужно найти самый большой элемент, вы можете использовать функцию max() в Python.
print("-----5: Самая большая строка в списке--------------------")
largest_string = max(languages)
print("The largest string is:", largest_string)
print("-----6: Max() В словарях---------------------------------")
square = {2: 4, -3: 9, -1: 1, -2: 4}
# the largest key
key1 = max(square)
print("The largest key:", key1)  # 2
# the key whose value is the largest
key2 = max(square, key=lambda k: square[k])
print("The key with the largest value:", key2)  # -3
# getting the largest value
print("The largest value:", square[key2])  # 9
# Во второй функции мы передали лямбда-функцию ключевому параметру.
