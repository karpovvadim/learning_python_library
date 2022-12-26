"""os.path.isdir(path)"""
# Возвратите True, если путь является существующим каталогом. Это следует за
# символическими ссылками, поэтому и islink(), и isdir() могут быть истинными для
# одного и того же пути.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.isdir('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
print(os.path.isdir('/home/vadim/python_library/File_and_Directory_Access/os.path'))
