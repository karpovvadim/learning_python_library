"""repr(object)"""
# Возвращает строку, содержащую печатное представление объекта. Для многих типов эта
# функция пытается возвратить строку, которая дала бы объект с тем же значением при
# передаче в eval(); в противном случае представление представляет собой строку,
# заключенную в угловые скобки, которая содержит имя типа объекта вместе с дополнительной
# информацией, часто включающей имя и адрес объекта. Класс может управлять тем, что
# эта функция возвращает для своих экземпляров, определяя метод __repr__().
# Если sys.displayhook() недоступен, эта функция вызовет RuntimeError.
var = 'foo'
var_2 = 1 + 2

print(repr(var))
print(repr(var_2))
print("-------реализовать __repr __() для настраиваемых объектов--------------")
# Внутренне функция repr() вызывает __repr __() данного объекта.
# Вы можете легко реализовать / переопределить __repr __(), чтобы repr() работал по-другому.
class Person:
    name = 'Adam'
    def __repr__(self):
        return repr('Hello ' + self.name )

print(repr(Person()))

""" class str(object=b'', encoding='utf-8', errors='strict')"""
# Возвращает строковую версию объекта. Если объект не указан, возвращает пустую строку.
# В противном случае поведение str() зависит от того, задана ли кодировка или ошибки,
# как показано ниже.
# Если не заданы ни кодировка, ни ошибки, str(object) возвращает type(object).__str__(object),
# который является «неформальным» или удобным для печати строковым представлением объекта.
# Для строковых объектов это сама строка. Если у объекта нет метода __str__(), то str()
# возвращается к возврату repr(object).
# Если указана хотя бы одна из кодировок или ошибок, объект должен быть байтоподобным
# объектом (например, bytes или bytearray). В этом случае, если объект является объектом
# bytes (или bytearray), то str(bytes, encoding, errors) эквивалентен bytes.decode(encoding,
# errors). В противном случае объект bytes, лежащий в основе объекта буфера, получается до
# вызова bytes.decode(). См. Типы двоичных последовательностей — bytes, bytearray,
# memoryview и Buffer Protocol для получения информации об объектах буфера.
# Передача объекта bytes в функцию str() без аргументов кодирования или ошибок подпадает
# под первый случай возврата неформального строкового представления (см. также параметр
# командной строки -b для Python).
# Есть шесть типов ошибок:
# 1. strict — ответ по умолчанию, который вызывает исключение UnicodeDecodeError при сбое
# 2. ignore — игнорирует некодируемый Unicode из результата
# 3. replace — заменяет некодируемый Unicode на вопросительный знак
# 4. xmlcharrefreplace — вставляет ссылку на символ XML вместо некодируемого Unicode
# 5. backslashreplace — вставляет последовательность символов \ uNNNN вместо некодируемого Unicode
# 6. namereplace — вставляет escape-последовательность \ N {…} вместо некодируемого Unicode
print("-------преобразовать в строку---------------------------")
print("str(10):  ", str(10))
print("str('Adam'):   ", str('Adam'))
print("str(b'Zoot!'): ", str(b'Zoot!'))
print("------Как str() работает с байтами?--------------------")
b = bytes('pythön', encoding='utf-8')
print(b)
print(str(b, encoding='ascii', errors='ignore'))
# Здесь символ «ö» не может быть декодирован с помощью ASCII. Следовательно, он должен
# выдать ошибку. Однако мы установили error = ‘ignore’. Следовательно, Python игнорирует
# символ, который не может быть декодирован с помощью str().
# Строки реализуют все общие операции с последовательностями, а также дополнительные методы,
# описанные ниже.
# Строки также поддерживают два стиля форматирования строк, один из которых обеспечивает
# большую степень гибкости и настройки (см. str.format(), Форматирование синтаксиса строки
# и пользовательское форматирование строк), а другой основан на форматировании стиля C
# printf, который обрабатывает более узкий диапазон типов. и его немного сложнее использовать
# правильно, но часто он быстрее для случаев, с которыми он может справиться (форматирование
# строк в стиле printf).
# Раздел Text Processing Services стандартной библиотеки охватывает ряд других модулей,
# предоставляющих различные утилиты, связанные с текстом (включая поддержку регулярных
# выражений в модуле re).
print(bytes("Bytes Байты:", encoding='utf-8'))
print("Bytes Байты:", str(bytes("Bytes Байты", encoding='utf-8')))
print("Bytes Байты:", str(bytes("Bytes Байты", encoding='utf-8'), encoding='ascii', errors='ignore'))
print("Bytes Байты:", str(bytes("Bytes Байты", encoding='utf-8'), encoding='UTF-8'))
