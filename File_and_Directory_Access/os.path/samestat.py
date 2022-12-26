"""os.path.samestat(stat1, stat2)"""
# Верните True, если кортежи статистики stat1 и stat2 ссылаются на один и тот же файл.
# Эти структуры могли быть возвращены функциями os.fstat(), os.lstat() или os.stat().
# Эта функция реализует базовое сравнение, используемое функциями samefile() и
# sameopenfile().
# Доступность: Unix, Windows.
# Изменено в версии 3.4: Добавлена поддержка Windows.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os
import pathlib

path1 = '/home/vadim/python_library/File_and_Directory_Access/os.path/samestat.py'
path2 = '/home/vadim/python_library/File_and_Directory_Access/os.path/sameopenfile.py'
stat1 = os.stat(path1)
fd = os.open(path1, os.O_RDONLY)
stat2 = os.fstat(fd)
print(os.path.samestat(stat1, stat2))
# True
p = pathlib.Path(path1)
stat3 = p.stat()
print(os.path.samestat(stat2, stat3))
# True
stat4 = os.stat(path2)
print(os.path.samestat(stat1, stat4))
# False
