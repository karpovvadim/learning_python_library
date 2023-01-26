"""reversed(seq)"""
# Вернуть обратный итератор. seq должен быть объектом, который имеет метод __reversed__()
# или поддерживает протокол последовательности (метод __len__() и метод __getitem__() с
# целочисленными аргументами, начинающимися с 0).
# for string
seq_string = 'Python'
print(list(reversed(seq_string)))
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')  # for tuple
print(tuple(reversed(seq_tuple)))
seq_range = range(5, 9)
print(list(reversed(seq_range)))  # for range
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))  # for list
class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v)))
