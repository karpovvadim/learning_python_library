"""str.partition(sep)"""    # разделять
# Возвращает копию строки, в которой каждый символ разделяет строку при первом вхождении
# sep, и возвращает тройку, содержащую часть до разделителя, сам разделитель и часть после
# разделителя. Если разделитель не найден, верните тройку, содержащую саму строку,
# за которой следуют две пустые строки.

string = "Python is fun"
print(string.partition('is '))  # 'is' separator is found
print(string.partition('not '))  # 'not' separator is not found
string = "Python is fun, isn't it"
print(string.partition('is'))  # splits at first occurence of 'is'
