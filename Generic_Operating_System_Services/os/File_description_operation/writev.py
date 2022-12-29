"""os.writev(fd, buffers)"""
# Записать содержимое буферов в файловый дескриптор fd. буферы должны быть
# последовательностью объектов, подобных байтам. Буферы обрабатываются в порядке
# массива. Все содержимое первого буфера записывается перед переходом ко второму и
# так далее.
# Возвращает общее количество фактически записанных байтов.
# Операционная система может установить ограничение (значение sysconf() 'SC_IOV_MAX')
# на количество используемых буферов.
#      Доступность: Юникс.
#      Новое в версии 3.3.
import os

path = "./file2.txt"

# Create a file and get the
# file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_CREAT | os.O_WRONLY)

# Bytes-like objects
# the data to be written in the file
buffer1 = bytearray(b"GeeksForGeeks: ")
buffer2 = bytearray(b"A computer science portal ")
buffer3 = bytearray(b"for geeks")

# write the data contained in
# bytes-like objects
# to the file descriptor fd
# using os.writev() method
numBytes = os.writev(fd, [buffer1, buffer2, buffer3])
# print the content of file
with open(path) as f:
    print(f.read())
# Print the number of bytes actually written
print("Total Number of bytes actually written:", numBytes)
