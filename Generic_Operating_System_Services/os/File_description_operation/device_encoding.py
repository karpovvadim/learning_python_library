"""os.device_encoding(fd)"""
# Возвращает строку, описывающую кодировку устройства, связанного с fd, если оно
# подключено к терминалу; иначе вернуть None.
# В Unix, если режим Python UTF-8 включен, возвращайте «UTF-8», а не кодировку устройства.
# Изменено в версии 3.10: в Unix функция теперь реализует режим Python UTF-8.
import os

path = "file.txt"

fd = os.open(path, os.O_RDWR | os.O_CREAT)

# Check if file descriptor fd
# is open and connected
# to a terminal using os.isatty() method
print("Connected to a terminal:", os.isatty(fd))

# Print the encoding of
# the device associated with
# the file descriptor fd
# using os.device_encoding() method
print("Device encoding:", os.device_encoding(fd))

# Open a new pseudo-terminal pair
# using os.openpty() method
# It will return master and slave
# file descriptor for
# pty ( pseudo terminal device) and
# tty ( native terminal device) respectively
master, slave = os.openpty()

# Check if file descriptor master
# is open and connected
# to a terminal using os.isatty() method
print("Connected to a terminal:", os.isatty(master))

# Print the encoding of
# the device associated with
# the file descriptor master
# using os.device_encoding() method
print("Device encoding:", os.device_encoding(master))
