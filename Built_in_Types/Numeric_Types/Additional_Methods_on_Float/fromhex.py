
# Два метода поддерживают преобразование в шестнадцатеричные строки и обратно.
# Поскольку числа с плавающей запятой в Python хранятся внутри как двоичные числа,
# преобразование числа с плавающей запятой в десятичную строку или из неё обычно
# связано с небольшой ошибкой округления. Напротив, шестнадцатеричные строки позволяют
# точное представление и спецификацию чисел с плавающей запятой. Это может быть
# полезно при отладке и числовой работе.

""" float.hex()"""
# Возвращает представление числа с плавающей запятой в виде шестнадцатеричной строки.
# Для конечных чисел с плавающей запятой это представление всегда будет включать
# начальный 0x и конечный p и показатель степени.

print(float.hex(3740.0))
print(float.hex(3740.5554))

""" classmethod float.fromhex(s)"""
# Метод класса для возврата числа с плавающей запятой, представленного шестнадцатеричной
# строкой s. Строка s может иметь начальные и конечные пробелы.
# Обратите внимание, что float.hex() — это метод экземпляра,
# а float.fromhex() — метод класса.
# Шестнадцатеричная строка принимает форму:
""" [sign] ['0x'] integer ['.' fraction] ['p' exponent] """
""" [знак] ['0x'] целое число ['.' дробь] [показатель 'p'] """
# где необязательный sign может быть либо +, либо -, integer и fraction — это строки
# шестнадцатеричных цифр, а exponent — десятичное целое число с необязательным
# начальным знаком. Регистр не имеет значения, и в целой или дробной части должна быть
# хотя бы одна шестнадцатеричная цифра. Этот синтаксис аналогичен синтаксису, указанному
# в разделе 6.4.4.2 стандарта C99, а также синтаксису, используемому в Java 1.5 и новее.
# В частности, вывод float.hex() можно использовать как шестнадцатеричный литерал с
# плавающей запятой в коде C или Java, а шестнадцатеричные строки, созданные символом
# формата C %a или Double.toHexString Java, принимаются float.fromhex().
# Обратите внимание, что показатель степени записывается в десятичном виде, а не в
# шестнадцатеричном, и что он даёт степень 2, на которую следует умножить коэффициент.
# Например, шестнадцатеричная строка 0x3.a7p10 представляет собой число с плавающей
# запятой (3 + 10./16 + 7./16**2) * 2.0**10 или 3740.0:

print(float.fromhex('0x3.a7p10'))  # 3740.0

# Применение обратного преобразования к 3740.0 даёт другую шестнадцатеричную строку,
# представляющую то же число:

print(float.hex(3740.0))   # '0x1.d380000000000p+11'

print("\n", float.fromhex('0x1.00p10'))  # 1024.0