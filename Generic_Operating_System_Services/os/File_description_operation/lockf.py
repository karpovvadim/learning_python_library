"""os.lockf(fd, cmd, len)"""
# Применить, проверить или снять блокировку POSIX для дескриптора открытого файла.
# fd — это дескриптор открытого файла. cmd указывает используемую команду — одну
# из F_LOCK, F_TLOCK, F_ULOCK или F_TEST. len указывает раздел файла для блокировки.
# Вызывает событие аудита os.lockf с аргументами fd, cmd, len.
# Доступность: Юникс.

# os.F_LOCK
# os.F_TLOCK
# os.F_ULOCK
# os.F_TEST
# Флаги, указывающие, какое действие будет выполнять функция lockf().
# Новое в версии 3.3.
import os

fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

os.write(fd, b"This is test")

os.lockf(fd, os.F_LOCK, 2)

print("Returned value is: ")

os.close(fd)
