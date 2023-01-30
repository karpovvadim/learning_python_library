"""str.center(width[, fillchar])"""
# Возврат по центру в строке длины ширины. Заполнение выполняется с использованием
# указанного символа заполнения (по умолчанию используется пробел ASCII).
# Исходная строка возвращается, если ширина меньше или равна len(s).
string = "Python is awesome"
new_string = string.center(24)
print("Centered String:", new_string)
new_string_2 = string.center(24, '*')
print("Centered String:", new_string_2)
