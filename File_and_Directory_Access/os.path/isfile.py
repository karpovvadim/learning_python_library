"""os.path.isfile(path)"""
# Возвратите True, если путь является существующим обычным файлом. Это следует за
# символическими ссылками, поэтому и islink(), и isfile() могут быть истинными для
# одного и того же пути.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.isfile('/home/vadim/python_library/File_and_Directory_Access/os.path/note.txt'))
print(os.path.isfile('/home/vadim/python_library/File_and_Directory_Access/os.path'))

