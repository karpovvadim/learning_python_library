"""os.get_blocking(fd)"""
# Получить режим блокировки файлового дескриптора: False, если установлен флаг O_NONBLOCK,
# True, если флаг снят.
# См. также set_blocking() и socket.socket.setblocking().
# Доступность: Юникс.
# Эта функция ограничена на Emscripten и WASI, см. Платформы WebAssembly для получения дополнительной информации.
# Новое в версии 3.5.
import os

path = "file.txt"

# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_RDWR)

# Get the blocking mode
# of the file descriptor
# using os.get_blocking() method
mode = os.get_blocking(fd)

if mode:
    print("File descriptor is in blocking mode")
else:
    print("File descriptor is in Non-blocking mode")

# Close the file descriptor
os.close(fd)
