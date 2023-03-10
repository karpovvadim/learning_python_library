""" class tuple([iterable])"""
# Кортежи могут быть созданы разными способами:
#         1. Использование пары круглых скобок для обозначения пустого кортежа: ()
#         2. Использование завершающей запятой для одноэлементного кортежа: a, или (a,)
#         3. Разделение элементов запятыми: a, b, c или (a, b, c)
#         4. Использование встроенного tuple(): tuple() или tuple(iterable)

# Конструктор создаёт кортеж, элементы которого совпадают и находятся в том же порядке,
# что и элементы iterable. iterable может быть либо последовательностью, контейнером,
# поддерживающим итерацию, либо объектом-итератором. Если iterable объект уже является
# кортежем, он возвращается без изменений. Например, tuple('abc') возвращает ('a', 'b', 'c'),
# а tuple( [1, 2, 3] ) возвращает (1, 2, 3). Если аргумент не указан, конструктор создаёт
# новый пустой кортеж ().
t1 = ()
t2 = 'a',
t3 = 'a', 'b', 'c',
t4 = tuple(range(5))
t5 = tuple()
print('\n', t1, '\n', t2, '\n', t3, '\n', t4, '\n', t5)

# Обратите внимание, что на самом деле кортеж составляет запятая, а не круглые скобки.
# Скобки необязательны, за исключением случая пустого кортежа или когда они необходимы во
# избежание синтаксической двусмысленности. Например, f(a, b, c) — это вызов функции с тремя
# аргументами, а f((a, b, c)) — это вызов функции с трехкомпонентным кортежем в качестве
# единственного аргумента.

#     Кортежи реализуют все общие операции последовательности.

# Для разнородных коллекций данных, где доступ по имени более нагляден, чем доступ по индексу,
# collections.namedtuple() может быть более подходящим выбором, чем простой объект кортежа.
