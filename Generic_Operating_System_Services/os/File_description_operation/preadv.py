"""os.preadv(fd, buffers, offset, flags=0)"""
# Чтение из дескриптора файла fd в позиции смещения в изменяемые буферы байтоподобных
# объектов, оставляя смещение файла неизменным. Передавайте данные в каждый буфер, пока он
# не заполнится, а затем переходите к следующему буферу в последовательности для хранения
# остальных данных.
# Аргумент flags содержит побитовое ИЛИ нуля или более из следующих флагов:
"""
    RWF_HIPRI
    RWF_NOWAIT
"""
# Возвращает общее количество фактически прочитанных байтов, которое может быть меньше
# общей емкости всех объектов.
# Операционная система может установить ограничение (значение sysconf() 'SC_IOV_MAX') на
# количество используемых буферов.
# Объедините функциональность os.readv() и os.pread().
# Доступность: Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX >= 7.1.
# Для использования флагов требуется Linux >= 4.6.
# Новое в версии 3.7.

"""os.RWF_NOWAIT"""
# Не ждите данных, которые не доступны немедленно. Если этот флаг указан, системный вызов
# вернется немедленно, если ему нужно будет прочитать данные из резервного хранилища или
# дождаться блокировки.
# Если некоторые данные были успешно прочитаны, он вернет количество прочитанных байтов.
# Если ни один байт не был прочитан, он вернет -1 и присвоит errno значение errno.EAGAIN.
# Доступность: Linux >= 4.14.
# Новое в версии 3.7

""" os.RWF_HIPRI"""
# Чтение/запись с высоким приоритетом. Позволяет блочным файловым системам использовать
# опрос устройства, что обеспечивает меньшую задержку, но может использовать
# дополнительные ресурсы.
# В настоящее время в Linux эту функцию можно использовать только для дескриптора файла,
# открытого с помощью флага O_DIRECT.
#      Доступность: Linux >= 4.6.
#      Новое в версии 3.7.
import os

# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open("Python_intro.txt", os.O_RDONLY)

# Number of bytes to be read
n = 50

# Read at most n bytes from
# file descriptor fd
# using os.read() method
readBytes = os.read(fd, n)

# Print the bytes read
print(readBytes)

buffers = 'high level'
# Now set the Offset value
offset = b'programming langua'
# Read at most n bytes from
# file descriptor fd at a position of
# given offset value using os.pread() method
readBytes = os.preadv(fd, buffers, offset, os.RWF_NOWAIT)

# Print the bytes read
print(readBytes)

# close the file descriptor
os.close(fd)
