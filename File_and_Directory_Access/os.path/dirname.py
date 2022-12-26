"""os.path.dirname(path)"""
# Возвращает имя каталога в пути path. Это первый элемент пары, возвращаемый путем
# передачи пути функции os.path.split()..
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.dirname('/home/User/Documents/file.txt'))
print(os.path.dirname('file.txt'))
print(os.path.dirname('/home/User/Documents'))

