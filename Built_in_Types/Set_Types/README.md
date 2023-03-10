Набор объектов — это неупорядоченная коллекция различных хешируемых объектов. Обычное
использование включает проверку принадлежности, удаление дубликатов из последовательности
и вычисление математических операций, таких как пересечение, объединение, разность и
симметричная разность. (Для других контейнеров см. встроенные классы dict, list и tuple,
а также модуль collections.)
Как и другие коллекции, наборы поддерживают x in set, len(set), и for x in set. Будучи
неупорядоченной коллекцией, наборы не записывают позицию элемента или порядок вставки.
Соответственно, наборы не поддерживают индексирование, нарезку или другое поведение,
подобное последовательности.
В настоящее время существует два встроенных типа набора: set and frozenset. Тип set
является изменяемым — содержимое можно изменить с помощью таких методов, как add() и remove().
Поскольку он является изменяемым, он не имеет хеш-значения и не может использоваться ни как
ключ словаря, ни как элемент другого набора. Тип замороженного набора является неизменяемым
и хешируемым — его содержимое нельзя изменить после его создания; поэтому его можно
использовать как ключ словаря или как элемент другого набора.
Непустые наборы (не замороженные наборы) можно создать, поместив список элементов, разделенных
запятыми, в фигурные скобки, например: {'jack', 'sjoerd'}, в дополнение к конструктору набора.
Конструкторы обоих классов работают одинаково:
    class set([iterable])
    class frozenset([iterable])

Возвращает новый объект set или frozenset, элементы которого взяты из iterable. Элементы множества должны быть хэшируемы. Для представления множества множеств внутренние множества должны быть объектами frozenset. Если iterable не указана, возвращается новое пустое множество.

Множества можно создавать несколькими способами:
    Используя список элементов, разделенных запятыми, в фигурных скобках: {'jack', 'sjoerd'}
    Используя множественное включение: {c for c in 'abracadabra' if c not in 'abc'}
    Используя конструктор типов: set(), set('foobar'), set(['a', 'b', 'foo'])

Экземпляры set и frozenset предоставляют следующие операции:

len(s)
    Возвращает количество элементов в множестве s (количество элементов s).

x in s
    Проверить x на принадлежность к s.

x not in s
    Проверить x на непринадлежность к s.

isdisjoint(other)¶
    Возвращает True, если у множества нет общих элементов с other. Множества не пересекаются тогда и только тогда, когда их пересечение — пустое множество.

issubset(other)
set <= other
    Проверить, каждый ли элемент в множестве состоит из other.

set < other
    Проверить, является ли множество правильным подмножеством other, то есть set <= other and set != other.

issuperset(other)
set >= other
    Проверить, есть ли в множестве все other элементы.

set > other
    Проверить, является ли множество подходящим надмножеством other, то есть set >= other and set != other.

union(*others)
set | other |...
    Возвращает новое множество с элементами из множества и всеми остальными.

intersection(*others)
set & other & ...
    Возвращает новое множество с элементами, общими для множества и всех остальных.

difference(*others)
set - other - ...
    Возвращает новое множество с элементами в множестве, которых нет в других.

symmetric_difference(other)
set ^ other
    Возвращает новое множество с элементами либо в множестве, либо в other, но не с обоими.

copy()
    Возвращает неглубокую копию множества.

Обратите внимание, что неоператорные версии методов union(), intersection(), difference()
и symmetric_difference(), issubset() и issuperset() принимают любой итеративный аргумент
в качестве аргумента. Напротив, их аналоги, основанные на операторах, требуют, чтобы их
аргументы были установлены. Это исключает подверженные ошибкам конструкции, такие как
set('abc') & 'cbs', в пользу более удобочитаемого set('abc').intersection('cbs').

Оба set и frozenset поддерживают множество для сравнения. Два множества равны тогда и
только тогда, когда каждый элемент каждого множества содержится в другом (каждый является
подмножеством другого). Набор меньше другого множества тогда и только тогда, когда первое
множество является соответствующим подмножеством второго множества (является подмножеством,
но не равны). Множество больше другого множества тогда и только тогда, когда первое
множество является соответствующим надмножеством второго множества (является надмножеством,
но не равно).

Экземпляры set сравниваются с экземплярами frozenset на основе их элементов. Например,
set('abc') == frozenset('abc') возвращает True, а также
set('abc') in set([frozenset('abc')]).

Сравнение подмножества и равенства не распространяется на функцию общего порядка. Например,
любые два непустых непересекающихся множества не равны и не являются подмножествами друг
друга, поэтому все следующие возвращают False: a<b, a==b или a>b.

Поскольку множества определяют только частичное упорядочение (отношения подмножеств),
выходные данные метода list.sort() не определены для списков множеств.

Элементы множества, такие как ключи словаря, должны быть хэшируемы.

Двоичные операции, которые смешивают экземпляры set с frozenset, возвращают тип первого
операнда. Например: frozenset('ab') | set('bc') возвращает экземпляр frozenset.

В следующей таблице перечислены операции, доступные для set, которые не применяются к
неизменяемым экземплярам frozenset:

update(*others)
set |= other | ...
    Обновить множество, добавив элементы из всех остальных.

intersection_update(*others)
set &= other & ...
    Обновить множество, сохранив только элементы, найденные в нём и все остальные.

difference_update(*others)
set -= other | ...
    Обновляет множество, удалив элементы, найденные в других.

symmetric_difference_update(other)
set ^= other
    Обновляет множество, сохранив только элементы, найденные в любом множестве, но не в обоих.

add(elem)
    Добавляет элемент elem в множество.

remove(elem)
    Удаляет элемент elem из множества. Вызывает KeyError, если elem не содержится в множестве.

discard(elem)
    Удаляет элемент elem из множества, если он присутствует.

pop()
    Удаляет и возвращает произвольный элемент из множества. Вызывает KeyError, если множество пусто.

clear()
    Убирает все элементы из множества.

Обратите внимание, что неоператорные версии методов update(), intersection_update(),
difference_update() и symmetric_difference_update() принимают любую итерацию в качестве
аргумента.

Обратите внимание, что аргумент elem для методов __contains__(), remove() и discard() может
быть набором. Чтобы облегчить поиск эквивалентного Frozenset, из elem создаётся временный.
