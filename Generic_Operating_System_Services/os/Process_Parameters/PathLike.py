""" class os.PathLike"""     # Параметры процесса
# Абстрактный базовый класс для объектов, представляющих путь к файловой системе,
# например. pathlib.PurePath.
# Новое в версии 3.6.
# абстрактный метод __fspath__()
# Возвращает представление пути файловой системы к объекту.
# Метод должен возвращать только объект str или bytes, предпочтение отдается str.
import os


class My_Path(os.PathLike):
    def __fspath__(self):
        path_1 = "/home/vadim/python_library/os/fspath.py"
        print(path_1)


path = My_Path()
path.__fspath__()
