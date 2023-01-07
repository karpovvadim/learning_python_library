"""os.chdir(path)"""
# Смена рабочей директории из кода.
# Измените текущий рабочий каталог на path.
# Эта функция может поддерживать указание файлового дескриптора dir_fd.
# Новое в версии 3.3: Добавлена поддержка указания пути в качестве файлового дескриптора на некоторых платформах.
# Изменено в версии 3.6: принимает объект, подобный пути.
# Параметры:
#     path - str, путь файловой системы.
# Возвращаемое значение:
#     None
# Описание:
# Функция chdir() модуля os изменяет текущий рабочий каталог. Аргумент path может
# принимать объекты, представляющие путь файловой системы, такие как pathlib.PurePath.
# Эта функция может поддерживать указание дескриптора файла dir_fd. Дескриптор должен
# ссылаться на открытый каталог, а не на открытый файл.
# Эта функция может вызывать исключение OSError и подклассы, такие как FileNotFoundError,
# PermissionError и NotADirectoryError.
# Вызывает событий аудита os.chdir с аргументом path.
import os
path = os.getcwd()
print("1_os.getcwd():", os.getcwd())  # распечатать текущий каталог
os.chdir(os.pardir)  # изменить текущий рабочий каталог на указанный путь
print("2_os.getcwd():", os.getcwd())  # проверьте путь, используя getcwd()
# изменим ещё раз текущий рабочий каталог
os.chdir(os.pardir)
print("3_os.getcwd():", os.getcwd())  # распечатать текущий каталог


""" os.fchdir(fd)"""
# Измените текущий рабочий каталог на каталог, представленный файловым дескриптором
# fd. Дескриптор должен относиться к открытому каталогу, а не к открытому файлу.
# Начиная с Python 3.3, это эквивалентно os.chdir(fd).
# Вызывает событие аудита (auditing event) os.chdir с аргументом path.
#       Доступность: Юникс.
print("----Использование метода os.fchdir() для изменения текущего рабочего каталога---")
print(os.getcwd())
path_1 = '..'
fd = os.open(path_1, os.O_RDONLY)
os.fchdir(fd)
print("Current working directory changed")
print(os.getcwd())

print("------Обработка возможных ошибок при использовании метода os.fchdir()-------")
fp = "file4.txt"
try:
    fd = os.open(fp, os.O_RDONLY)
    try:
        os.fchdir(fd)
        print("Current working directory changed")
        print("Current working directory:", os.getcwd())
    # Catch exceptions if file descriptor does not represents a directory
    # Перехватывать исключения, если файловый дескриптор не представляет каталог
    except NotADirectoryError:
        print("The given file descriptor does not represent a directory")
        # Данный файловый дескриптор не представляет каталог
# Catch exceptions If path does not exists
# Перехватывать исключения, если путь не существует
except FileNotFoundError:
    print("Path does not exists")
# If there is any permission related issue while opening the given path
# Если при открытии данного пути возникает какая-либо проблема, связанная с разрешением
except PermissionError:
    print("Permission denied")  # Доступ запрещен
