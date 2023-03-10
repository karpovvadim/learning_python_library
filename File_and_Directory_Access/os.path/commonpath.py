"""os.path.commonpath(paths)"""
# Возвращает самый длинный общий подпуть каждого имени пути в путях последовательности.
# Поднимите ValueError, если пути содержат как абсолютные, так и относительные пути,
# пути находятся на разных дисках или пути пусты. В отличие от commonprefix(),
# это возвращает правильный путь.
#      Доступность: Unix, Windows.
#      Новое в версии 3.5.
#      Изменено в версии 3.6: принимает последовательность объектов, подобных пути.
# Параметры:
#     paths - последовательности путей файловой системы.
# Возвращаемое значение:
#     общий подпуть списка путей файловой системы.
# Описание:
# Функция commonpath() модуля os.path возвращает самый длинный общий подпуть каждого
# пути в последовательности paths. Если последовательность paths содержит как
# абсолютные так и относительные пути, пустые пути или пути находящиеся на разных
# дисках, то возникает исключение ValueError.
# Элементы последовательности paths могут быть только байты или только строки.
# Результатом будет является тот же тип.
# Функция os.path.commonpath() может принимать объект, представляющий путь к
# файловой системе, например такой как pathlib.PurePath.
# В отличие от функции os.path.commonprefix(), os.path.commonpath() возвращает
# правильный путь.
import os.path
print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))

