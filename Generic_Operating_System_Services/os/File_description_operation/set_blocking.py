"""os.set_blocking(fd, blocking)"""
# Установить режим блокировки указанного файлового дескриптора. Установите флаг
# O_NONBLOCK, если блокировка имеет значение False, в противном случае снимите флаг.
#     См. также get_blocking() и socket.socket.setblocking().
#     Доступность: Юникс.
# Эта функция ограничена на Emscripten и WASI, см. Платформы WebAssembly для получения
# дополнительной информации.
#     New in version 3.5.
import os
# File path
path = "file.txt"

# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_RDWR)
# Get the current blocking mode
# of the file descriptor
# using os.get_blocking() method
print("Blocking Mode:", os.get_blocking(fd))

# Change the blocking mode
blocking = False
os.set_blocking(fd, blocking)
print("Blocking mode changed")
# Get the blocking mode
# of the file descriptor
# using os.get_blocking() method
print("Blocking Mode:", os.get_blocking(fd))
# close the file descriptor
os.close(fd)
# A False value for blocking
# mode denotes that the file
# descriptor has been put into
# Non-Blocking mode while True
# denotes that file descriptor
# is in blocking mode.
