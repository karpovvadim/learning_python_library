"""os.path.getctime(path)"""
# Возвращает ctime системы, которое в некоторых системах (например, Unix) является
# временем последнего изменения метаданных, а в других (например, Windows) —
# временем создания пути. Возвращаемое значение — это число, указывающее количество
# секунд, прошедших с начала эпохи (см. модуль времени). Поднимите OSError, если
# файл не существует или недоступен.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
import time
print(os.path.getctime('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
ctime = os.path.getctime('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt')
print(time.ctime(ctime))
ctime = os.path.getctime('/home/vadim/python_library/File_and_Directory_Access/os.path/getatime.py')
print(time.ctime(ctime))
