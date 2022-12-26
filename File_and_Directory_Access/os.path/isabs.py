"""os.path.isabs(path)"""
# Возвратите True, если путь является абсолютным путем. В Unix это означает, что он
# начинается с косой черты, в Windows — с (обратной) косой черты после отсечения
# потенциальной буквы диска.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.isabs('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
print(os.path.isabs(b'/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
print(os.path.isabs('home/vadim/python_library/File_and_Directory_Access/os.path/getatime.py'))
print(os.path.isabs('../vadim/python_library/File_and_Directory_Access/os.path/1_overview.txt'))
