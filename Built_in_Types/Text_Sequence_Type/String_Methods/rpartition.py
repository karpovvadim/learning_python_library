"""str.rpartition(sep)"""  # разделять
# Разделить строку на последнее вхождение sep и вернуть кортеж из трёх частей, содержащий
# часть перед разделителем, сам разделитель и часть после разделителя. Если разделитель не
# найден, вернуть 3-кортеж, содержащий две пустые строки, за которыми следует сама строка.

string = "Python is fun"
print(string.rpartition('is '))  # 'is' separator is found
print(string.rpartition('not '))  # 'not ' separator is not found
string = "Python is fun, isn't it"
print(string.rpartition('is'))  # splits at last occurence of 'is'
# (разбивается при последнем появлении 'is')
