""" class list(iterable)"""
# Список — это не функция, а изменяемый тип последовательности, как описано в разделе
# «Списки и типы последовательностей» — список, кортеж, диапазон.
# Параметры
# Конструктор принимает единственный аргумент:
# iterable (необязательно) — объект, который может быть последовательностью (строка, кортежи)
# или коллекцией (набор, словарь) или любым объектом итератора.
# Возвращаемое значение из списка
# Конструктор list() возвращает список:
# Если параметры не переданы, возвращается пустой список.
# Если итерируемый передается в качестве параметра, он создает список,
# состоящий из итерируемых элементов.
print("---0---Создание списков из строки, кортежа и списка-------------")
# empty list
print(list())
# vowel string
vowel_string = 'aeiou'
print(list(vowel_string))
# vowel tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))
# vowel list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))
print("---1----Создание списков из набора и словаря---------------------")
# vowel set
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set))
# vowel dictionary
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print(list(vowel_dictionary))
# Примечание. В случае словарей ключи будут элементами списка. Кроме того, порядок
# элементов будет случайным.
print("----2-----Создать список из объекта-итератора------------------------")
# objects of this class are iterators
class PowTwo:
    def __init__(self, maximum):
        self.max = maximum

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result

pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)
print(list(pow_two_iter))