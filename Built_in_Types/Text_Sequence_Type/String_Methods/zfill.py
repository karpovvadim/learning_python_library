"""str.zfill(width)"""   # заполнить
# Вернуть копию строки, заполненную цифрами ASCII '0', чтобы создать строку длины и ширины.
# Префикс начального знака ('+'/'-') обрабатывается путем вставки заполнения после символа
# знака, а не перед ним. Исходная строка возвращается, если ширина меньше или равна len(s).

print("42".zfill(5))
print("-42".zfill(5))
number = "-290"
print(number.zfill(8))
number = "+290"
print(number.zfill(8))
text = "--random+text"
print(text.zfill(20))
