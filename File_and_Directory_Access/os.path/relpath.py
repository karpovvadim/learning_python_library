"""os.path.relpath(path, start=os.curdir)"""
# Возвращает относительный путь к файлу из текущего каталога или из необязательного
# начального каталога. Это вычисление пути: к файловой системе не обращаются для
# подтверждения существования или характера пути или начала.
# В Windows ValueError возникает, когда путь и начало находятся на разных дисках.
# Для аргумента start по умолчанию запускается функция os.curdir.
# Аргумент path может принимать байтовые или текстовые строки. Результатом будет
# является тот же тип.
# Функция os.path.realpath() может принимать объект, представляющий путь к
# файловой системе, например такой как pathlib.PurePath.
# Доступность: Unix, Windows.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
path = "/home/vadim/Desktop/file.txt"
start = "/home/vadim/"
print(os.path.relpath(path, start))
# Desktop/file.txt
print(os.path.relpath(path))
start = "/home/docs-python/"
print(os.path.relpath(path, start))
# '../User/Desktop/file.txt'

start = "/home/docs-python/Docs"
print(os.path.relpath(path, start))
# '../../User/Desktop/file.txt'
