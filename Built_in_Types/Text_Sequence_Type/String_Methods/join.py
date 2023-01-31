"""str.join(iterable)"""   # соединиться c разделителем
# Возвращает строку, которая представляет собой конкатенацию строк в итерации. Ошибка
# TypeError будет вызвана, если в итерации есть какие-либо нестроковые значения, включая
# объекты байтов. Разделителем между элементами является строка, обеспечивающая этот метод.
# Сборка строки из списка с разделителем S.
# Функция принимает в качестве параметра итерацию (объекты, способные возвращать свои члены
# по одному).
# Вот некоторые из примеров итераций:
# 1. Собственные типы данных ‒ список, кортеж, строка, словарь и набор.
# 2. Файловые объекты и объекты, которые определены с помощью __iter __(), __getitem()__.

print("-------str.join(iterable)-----lists---tuples--------------------")
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))  # .join() with lists
numTuple = ('1', '2', '3', '4')  # .join() with tuples
print(separator.join(numTuple))

print("\n-----.join() with str------------------------------------")
s1 = 'abc'
s2 = '123'
print('s1.join(s2) =', 'abc'.join('123'))  # '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s2.join(s1) =', '123'.join('abc'))  # 'a'+ '123'+ 'b'+ '123'+ 'b'
print("' '.join(s2) =", ' '.join('123'))

print("\n-------str.join(iterable)---sets---с множествами------------------")
test = {'2', '1', '3'}
s = ', '
print(s.join(test))  # .join() with sets

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

print("\n-------str.join(iterable)----.join() with dictionaries--------")
test = {'mat': 1, 'that': 2}  # .join() with dictionaries
s = '=>'
print(s.join(test))  # joins the keys only

test = {1: 'mat', 2: 'that'}
s = ', '
print(s.join(test))    # this gives error since key isn't string
# Метод пытается соединить ключи (не значения) словаря с помощью разделителя строк.
# Примечание: Если ключ строки не является строкой, возникает исключение TypeError.
