"""
static bytes.maketrans(from, to)
static bytearray.maketrans(from, to)
"""
# Статический метод возвращает таблицу преобразования, используемую для bytes.translate(),
# которая будет отображать каждый символ в from в символ в той же позиции в to; from и to
# должны быть байтоподобными объектами и содержать одинаковую длину.

#    Добавлено в версии 3.1.
firstString = b"abc"
secondString = b"def"
string = b"123"
print(string.maketrans(firstString, secondString))
