# Возвращает длину (количество элементов) объекта. Аргумент может быть последовательностью
#  (such as a string, bytes, tuple, list, or range) (например, строкой, байтами, кортежем,
#  списком или диапазоном)  or a collection (such as a dictionary, set, or frozen set).
# или набором (например, словарем, набором или замороженным набором).
# Детали реализации CPython: len вызывает OverflowError на длинах, превышающих sys.maxsize,
# например range(2 ** 100).
print("---0-----Как работает с кортежами, списками и диапазоном?---------------------")
testList = []
print(testList, 'length is', len(testList))
testList = [1, 2, 3]
print(testList, 'length is', len(testList))
testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))
testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
print("---1---Как работает со строками и байтами?------------------------------------")
testString = ''
print('Length of', testString, 'is', len(testString))
testString = 'Python'
print('Length of', testString, 'is', len(testString))
# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))
testList = [1, 2, 3]
# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))
print("---2-------Как работает со словарями и наборами?-----------------------------")
testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))
testSet = set()   # Empty Set
print(testSet, 'length is', len(testSet))
testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))
testDict = {}
print(testDict, 'length is', len(testDict))
testSet = {1, 2}
frozenTestSet = frozenset(testSet)  # frozenSet
print(frozenTestSet, 'length is', len(frozenTestSet))
print("---3----Как работает с настраиваемыми объектами?-----------------------------")
class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number

s1 = Session()   # default length is 0
print(len(s1))
s2 = Session(6)  # giving custom length (представление нестандартной длины)
print(len(s2))
