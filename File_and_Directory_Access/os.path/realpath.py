"""os.path.realpath(path, *, strict=False)"""
# Возвращает канонический путь указанного имени файла, исключая любые символические
# ссылки, встречающиеся в пути (если они поддерживаются операционной системой).
# Если путь не существует или встречается цикл символической ссылки, а strict
# имеет значение True, возникает ошибка OSError. Если strict имеет значение False,
# путь разрешается, насколько это возможно, и любой остаток добавляется без
# проверки его существования.
# Примечание
# Эта функция эмулирует процедуру операционной системы для создания канонического
# пути, которая немного отличается в Windows и UNIX в отношении того, как
# взаимодействуют ссылки и последующие компоненты пути.
# API-интерфейсы операционной системы делают пути каноническими по мере
# необходимости, поэтому обычно нет необходимости вызывать эту функцию.
# Изменено в версии 3.6: принимает объект, подобный пути.
# Изменено в версии 3.8: символические ссылки и соединения теперь
# разрешаются в Windows.
# Изменено в версии 3.10: Добавлен параметр strict.
import os.path
import pathlib

p = pathlib.Path('file.txt')
# создадим файл
p.touch()
# канонический путь
path = os.path.realpath(p)
print(path)
# '/home/docs-python/file.txt'

# проверка символической ссылки
link = os.path.join(os.getcwd(), 'Desktop', 'link.txt')
print(link)
# '/home/docs-python/Desktop/link.txt'

# создадим символическую ссылку
os.symlink(path, link)
# канонический путь по ссылке
print(os.path.realpath(link, strict=True))
# '/home/docs-python/file.txt'
