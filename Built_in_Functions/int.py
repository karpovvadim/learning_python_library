# Возвращает целочисленный объект, созданный из числа или строки x, или возвращает 0,
# если аргументы не заданы. Если x определяет __int__(), int(x) возвращает x.__int__().
# Если x определяет __index__(), он возвращает x.__index__(). Если x определяет __trunc__(),
# он возвращает x.__trunc__(). Для чисел с плавающей запятой это усекается до нуля.
# Если x не является числом или если задано основание, то x должен быть строкой,
# байтами или экземпляром массива байтов, представляющим целочисленный литерал в
# системе счисления. При желании перед литералом может стоять + или - (без пробела между ними)
# и он может быть окружен пробелом. Литерал с основанием n состоит из цифр от 0 до n-1,
# где числа от a до z (или от A до Z) имеют значения от 10 до 35. База по умолчанию — 10.
# Допустимые значения: 0 и 2–36. Литералы с основанием 2, -8 и -16 могут дополнительно иметь
# префикс 0b/0B, 0o/0O или 0x/0X, как и целочисленные литералы в коде. База 0 означает
# интерпретировать точно как литерал кода, так что фактическая база равна 2, 8, 10 или 16,
# и поэтому int('010', 0) недопустимо, а int('010') допустимо, а также int('010', 8).
# Изменено в версии 3.4: если база не является экземпляром int и базовый объект имеет
# метод base.__index__, этот метод вызывается для получения целого числа для базы.
# Предыдущие версии использовали base.__int__ вместо base.__index__.
# Изменено в версии 3.6: допускается группировка цифр с подчеркиванием, как в литералах кода.
# Изменено в версии 3.7: x теперь является позиционным параметром.
# Изменено в версии 3.8: возвращается к __index__(), если __int__() не определен.
# Изменено в версии 3.11: делегирование __trunc__() устарело.
# Изменено в версии 3.11: строковые входные данные и представления строк могут быть ограничены,
# чтобы избежать атак типа «отказ в обслуживании». ValueError возникает, когда превышен предел
# при преобразовании строки x в целое число или когда преобразование целого числа в строку
# превысит предел. См. документацию по ограничению длины преобразования целочисленной строки.
# integer
print("int(123) is:", int(123))
# float
print("int(123.23) is:", int(123.23))
# string
print("int('123') is:", int('123'))
# binary 0b or 0B
print("For 1010, int is:", int('1010', 2))
print("For 0b1010, int is:", int('0b1010', 2))
# octal 0o or 0O
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))
# hexadecimal
print("For A, int is:", int('A', 16))
print("For 0xA, int is:", int('0xA', 16))
# Вы можете сделать это, переопределив методы __index __() и __int __() класса для возврата числа.
# Эти два метода должны возвращать то же значение, поскольку более старые версии Python
# используют __int __(), а более новые используют метод __index __().

class Person:
    age = 23

    def __index__(self):
        self.age = 41
        return self.age

    def __int__(self):
        self.age = 52
        return self.age

person = Person()
print('int(person) is:', int(person))