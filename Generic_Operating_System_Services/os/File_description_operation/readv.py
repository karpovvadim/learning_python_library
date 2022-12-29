"""os.readv(fd, buffers)"""
# Чтение из файлового дескриптора fd в несколько изменяемых байтовых буферов объектов.
# Передавайте данные в каждый буфер, пока он не заполнится, а затем переходите к
# следующему буферу в последовательности для хранения остальных данных.
# Возвращает общее количество фактически прочитанных байтов, которое может быть меньше
# общей емкости всех объектов.
# Операционная система может установить ограничение (значение sysconf() 'SC_IOV_MAX')
# на количество используемых буферов.
#    Доступность: Юникс.
#    Новое в версии 3.3.
import os

path = "./file.txt"

# Open the file and get the file descriptor associated with it using os.open() method
fd = os.open(path, os.O_RDONLY)
# Bytes-like objects to hold the data read from the file
size = 25
buffer1 = bytearray(size)
buffer2 = bytearray(size)
print('buffer1:', buffer1)
buffer3 = bytearray(size)
# Read the data from the file descriptor into bytes-like objects using os.readv() method
numBytes = os.readv(fd, [buffer1, buffer2, buffer3])
print("Data read in buffer 1:", buffer1.decode())  # Print the data read in buffer1
print("Data read in buffer 2:", buffer2.decode())  # Print the data read in buffer2
print("Data read in buffer 3:", buffer3.decode())  # Print the data read in buffer3
# Print the number of bytes actually read
print("\nTotal Number of bytes actually read:", numBytes)
