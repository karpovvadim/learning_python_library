"""os.readlink(path, *, dir_fd=None)"""
# Возвращает строку, представляющую путь, на который указывает символическая ссылка.
# Результатом может быть как абсолютный, так и относительный путь; если он
# относительный, его можно преобразовать в абсолютный путь с помощью
# os.path.join(os.path.dirname(path), result).
# Если путь является строковым объектом (напрямую или косвенно через интерфейс
# PathLike), результатом также будет строковый объект, и вызов может вызвать ошибку
# UnicodeDecodeError. Если путь является байтовым объектом (прямым или косвенным),
# результатом будет байтовый объект.
# Эта функция также может поддерживать пути относительно дескрипторов каталогов.
# При попытке разрешить путь, который может содержать ссылки, используйте realpath()
# для правильной обработки различий рекурсии и платформы.
# Доступность: Unix, Windows.
# Изменено в версии 3.2: Добавлена поддержка символических ссылок Windows 6.0 (Vista).
# Новое в версии 3.3: Аргумент dir_fd.
# Изменено в версии 3.6: принимает объект, подобный пути, в Unix.
# Изменено в версии 3.8: принимает объект, подобный пути, и объект байтов в Windows.
# Изменено в версии 3.8: добавлена поддержка соединений каталогов и изменено, чтобы
# возвращать путь подстановки (который обычно включает префикс \\?\), а
# не необязательное поле «печатное имя», которое возвращалось ранее.
import os
path = "/home/vadim/PycharmProjects/learning_python_library/" \
       "Generic_Operating_System_Services/os/Files_and_Directories/tt.txt"

# Create a symbolic link of above path using os.symlink() method
link = "tt_symbolic.txt"
try:
    os.symlink(path, link)
except OSError as error:
    print(error)
# So, link is a symbolic link. Now using os.readlink() method resolve the symbolic link
# Итак, ссылка является символической ссылкой. Теперь, используя метод os.readlink(),
# разрешаем символическую ссылку.
originalPath = os.readlink(link)
print("Symbolic link points to", originalPath)  # Символическая ссылка указывает на

# If the given path is not a symbolic link then os.readlink() method will
# raise an OSError (Если данный путь не является символической ссылкой,
# метод os.readlink() вызовет ошибку OSError).
