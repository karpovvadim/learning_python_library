"""os.posix_fallocate(fd, offset, len)"""
# Гарантирует, что для файла, указанного параметром fd, выделено достаточно места на диске,
# начиная со смещения и продолжая len байт.
#      Доступность: Unix, не Emscripten.
#      Новое в версии 3.3.
import os
# preallocate using os.posix_fallocate a 1kb file
# предварительно выделить с помощью os.posix_fallocate файл размером 1 КБ

fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)
os.posix_fallocate(fd, 0, 16)
