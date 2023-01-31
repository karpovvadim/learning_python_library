




print("--------str.rsplit(sep=None, maxsplit=- 1)----расколоть----------------")
# Возвращает список слов в строке, используя sep в качестве строки-разделителя. Если задано
# значение maxsplit, выполняется не более maxsplit, самые правые. Если sep не указан или
# None, любая строка пробела является разделителем. За исключением разделения справа,
# rsplit() ведет себя как split(), который подробно описан ниже.
text = 'Love thy neighbor'
print(text.rsplit())  # splits at space
grocery = 'Milk, Chicken, Bread'
print(grocery.rsplit(', '))  # splits at ','    распадается на
print(grocery.rsplit(':'))  # Splitting at ':'  Разделение на
grocery = 'Milk, Chicken, Bread, Butter'
print(grocery.rsplit(sep=', ', maxsplit=0))  # maxsplit: 0
print(grocery.rsplit(', ', 1))  # maxsplit: 1
print(grocery.rsplit(', ', 2))  # maxsplit: 2
print(grocery.rsplit(', ', 5))  # maxsplit: 5
print("--------str.split(sep=None, maxsplit=- 1)----расколоть----------------")
# Возвращает список слов в строке, используя sep в качестве строки-разделителя. Если
# указано значение maxsplit, выполняется не более maxsplit разбиений (таким образом, список
# будет содержать не более maxsplit+1 элементов). Если maxsplit не указан или равен -1,
# то ограничения на количество сплитов нет (делаются все возможные сплиты).
# Если указано значение sep, последовательные разделители не группируются и считаются
# разграничивающими пустые строки (например, '1,,2'.split(',') возвращает ['1', '', '2']).
# Аргумент sep может состоять из нескольких символов (например, '1<>2<>3'.split('<>')
# возвращает ['1', '2', '3']). Разделение пустой строки с указанным разделителем
# возвращает [''].
print('1,2,3'.split(','))
print('1,2,3'.split(',', maxsplit=1))
print('1,2,,3,'.split(','))
text = 'Love thy neighbor'   #  Возлюби ближнего твоего
print(text.split())         # splits at space
grocery = 'Milk, Chicken, Bread'
print(grocery.split(', '))  # splits at ','    распадается на
print(grocery.split(':'))  # Splitting at ':'  Разделение на
# Если sep не указан или равен None, применяется другой алгоритм разделения:
# последовательные пробелы рассматриваются как один разделитель, и результат не будет
# содержать пустых строк в начале или в конце, если в строке есть начальные или конечные
# пробелы. Следовательно, разделение пустой строки или строки, состоящей только из пробелов,
# с помощью разделителя None возвращает [].
print('1 2 3'.split())
print('1 2 3'.split(maxsplit=1))
print('   1   2   3   '.split())
grocery = 'Milk, Chicken, Bread, Butter'
print(grocery.split(', ', 0))  # maxsplit: 0
print(grocery.split(', ', 1))  # maxsplit: 1
print(grocery.split(', ', 2))  # maxsplit: 2
print(grocery.split(', ', 5))  # maxsplit: 5
