"""os.path.getatime(path)"""
# Возвращает время последнего доступа к пути (к файлу или каталогу). Возвращаемое
# значение представляет собой число с плавающей запятой, указывающее количество
# секунд, прошедших с начала эпохи (см.  модуль time). Поднимите OSError,
# если файл не существует или недоступен.
import os.path
import time
print(os.path.getatime('/home/vadim/python_library/File_and_Directory_Access/os.path/README.md'))
atime = os.path.getatime('/home/vadim/python_library/File_and_Directory_Access/os.path/README.md')
print(time.ctime(atime))
atime = os.path.getatime('/home/vadim/python_library/File_and_Directory_Access/os.path/getatime.py')
print(time.ctime(atime))
