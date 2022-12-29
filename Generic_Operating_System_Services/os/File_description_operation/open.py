# Операции с файловым дескриптором (File Descriptor Operations)
"""os.open(path, flags, mode=0o777, *, dir_fd=None)"""
# Откройте путь к файлу и установите различные флаги в соответствии с флагами и,
# возможно, его режим в соответствии с режимом. В режиме вычислений текущее значение
# umask сначала маскируется. Возвращает дескриптор файла для вновь открытого файла.
# Новый файловый дескриптор не подлежит наследованию. Описание значений флага и
# режима см. в документации по времени выполнения C; константы флагов (такие как
# O_RDONLY и O_WRONLY) определены в модуле os. В частности, в Windows добавление
# O_BINARY необходимо для открытия файлов в двоичном режиме.
# Эта функция может поддерживать пути относительно дескрипторов каталогов с
# параметром dir_fd.
# Вызывает открытое событие аудита с аргументами пути, режима и флагов.
# Изменено в версии 3.4: новый файловый дескриптор теперь не наследуется.
#      Примечание
# Эта функция предназначена для низкоуровневого ввода/вывода. Для обычного
# использования используйте встроенную функцию open(), которая возвращает файловый
# объект с помощью методов read() и write() (и многих других). Чтобы обернуть
# файловый дескриптор в файловый объект, используйте fdopen().
#      Новое в версии 3.3: Аргумент dir_fd.
#      Изменено в версии 3.5: если системный вызов прерывается, а обработчик сигнала
#      не вызывает исключение, функция теперь повторяет системный вызов вместо
#      создания исключения InterruptedError (обоснование см. в PEP 475).
#      Изменено в версии 3.6: принимает объект, подобный пути.
# Если системный вызов прерывается и обработчик сигнала не вызывает исключение,
# функция повторяет системный вызов, а не вызывает исключение InterruptedError
# Функция принимает объекты, реализующих интерфейс os.PathLike
# В следующем примере используется параметр dir_fd функции os.open(), чтобы открыть
# файл относительно данного каталога:
import os

path_1 = "/home/vadim/python_library/Generic_Operating_System_Services/os/File_description_operation/open.py"
dir_fd = os.open(path_1, os.O_RDONLY)
print(dir_fd)


def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)


with open('/home/vadim/python_library/Generic_Operating_System_Services/os/test.txt', 'w', opener=opener) as f:
    print('This will be written to /Generic_Operating_System_Services/os/test.txt', file=f)
os.close(dir_fd)  # не забываем закрыть файловый дескриптор.
# Опции для flags функции os.open()
# Следующие константы являются опциями для параметра flags функции os.open().
# Их можно объединить с помощью побитового оператора ИЛИ '|'. Некоторые из них
# доступны не на всех платформах. Описание их доступности и использования смотрите
# на странице руководства open(2) по Unix или по MSDN в Windows.
# Константы доступные в Unix и Windows:
#
#     os.O_RDONLY,
#     os.O_WRONLY,
#     os.O_RDWR,
#     os.O_APPEND,
#     os.O_CREAT,
#     os.O_EXCL,
#     os.O_TRUNC.
#
# Константы доступные только в Unix:
#
#     os.O_DSYNC,
#     os.O_RSYNC,
#     os.O_SYNC,
#     os.O_NDELAY,
#     os.O_NONBLOCK,
#     os.O_NOCTTY,
#     os.O_CLOEXEC.
#
# Константы доступные только в Windows:
#
#     os.O_BINARY,
#     os.O_NOINHERIT,
#     os.O_SHORT_LIVED,
#     os.O_TEMPORARY,
#     os.O_RANDOM,
#     os.O_SEQUENTIAL,
#     os.O_TEXT.
#
# Константы являются расширениями и не присутствуют, если они не определены библиотекой C:
#
#     os.O_ASYNC,
#     os.O_DIRECT,
#     os.O_DIRECTORY,
#     os.O_NOFOLLOW,
#     os.O_NOATIME,
#     os.O_PATH,
#     os.O_TMPFILE,
#     os.O_SHLOCK,
#     os.O_EXLOCK.
print("------------------------------------------------------")
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, b"This is test")

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
