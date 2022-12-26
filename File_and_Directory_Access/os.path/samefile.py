""" os.path.samefile(path1, path2)"""
# Верните True, если оба аргумента имени пути относятся к одному и тому же файлу
# или каталогу. Это определяется номером устройства и номером i-узла и вызывает
# исключение, если вызов os.stat() для любого имени пути завершается неудачно.
# Доступность: Unix, Windows.
# Изменено в версии 3.2: Добавлена поддержка Windows.
# Изменено в версии 3.4: Windows теперь использует ту же реализацию, что и все другие платформы.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path

path = '/home/docs-python/Desktop/file.txt'
link = '/home/docs-python/link.txt.txt'
os.symlink(path, link)
print(os.path.samefile(path, link))
# True
print(path1=os.path.join(os.getcwd(), 'Desktop', 'link.txt.txt'))
# True
print(os.path.samefile(path, path1))
# True
