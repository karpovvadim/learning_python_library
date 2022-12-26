"""os.path.getmtime(path)"""
# Возвращает время последней модификации пути. Возвращаемое значение представляет
# собой число с плавающей запятой, указывающее количество секунд, прошедших с начала
# эпохи (см. модуль времени). Поднимите OSError, если файл не существует или недоступен.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.getmtime('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
mtime = os.path.getmtime('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt')
import time
print(time.ctime(mtime))
mtime = os.path.getmtime('/home/vadim/python_library/File_and_Directory_Access/os.path/getatime.py')
print(time.ctime(mtime))
