"""os.close(fd)"""
# This function is intended for low-level I/O and must be applied to a file descriptor
# as returned by os.open() or pipe(). To close a “file object” returned by the built-in
# function open() or by popen() or fdopen(), use its close() method.
# Закройте файловый дескриптор fd.
# Примечание
# Эта функция предназначена для низкоуровневого ввода-вывода и должна применяться к
# файловому дескриптору, возвращаемому функциями os.open() или pipe(). Чтобы закрыть
# «файловый объект», возвращаемый встроенной функцией open(), popen() или fdopen(),
# используйте ее метод close().
import os

path = "close.txt"

# open the file and get the file descriptor associated with it using os.open() method
# открыть файл и получить связанный файловый дескриптор с помощью метода os.open()
fd = os.open(path, os.O_RDWR | os.O_CREAT)
print(fd)

# Perform some operation. Lets write a string.
# Выполнить некоторую операцию. Написать строку.
s = "GeeksForGeeks: A computer science portal for geeks"
# Компьютерщики для гиков: Портал информатики для гиков
# A computer science - Информатика

# Convert string to bytes object (Преобразовать строку в байтовый объект)
line = str.encode(s)

# Write string to file referred by   Записать строку в файл, на который ссылается
# by the file descriptor             по файловому дескриптору
os.write(fd, line)

# close the file descriptor
os.close(fd)
print("File descriptor closed successfully")