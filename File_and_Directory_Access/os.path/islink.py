"""os.path.islink(path)"""
# Возвратите True, если путь относится к существующей записи каталога, которая
# является символической ссылкой. Всегда False, если символические ссылки не
# поддерживаются средой выполнения Python.
# Изменено в версии 3.6: принимает объект, подобный пути.  Accepts a path-like object.
import os
import pathlib

# создадим файл
p = pathlib.Path('file.txt')
p.touch()
# создадим символьную ссылку
os.symlink(p, 'link.txt')

# ПРОВЕРКА
print(os.path.islink('link.txt'))
# True
print(os.path.islink('file.txt'))
# False

# Очистка
p.unlink()
os.unlink('link.txt')
print(os.path.islink('link.txt'))
