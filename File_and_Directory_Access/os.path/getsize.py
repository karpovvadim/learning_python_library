"""os.path.getsize(path)"""
# Возвращает размер пути в байтах. Поднимите OSError, если файл не существует или
# недоступен.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.getsize('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
print(os.path.getsize(b'/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
print(os.path.getsize('/home/vadim/python_library/File_and_Directory_Access/os.path/getatime.py'))

