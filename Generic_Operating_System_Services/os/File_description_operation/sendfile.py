""" os.sendfile(out_fd, in_fd, offset, count)"""
""" os.sendfile(out_fd, in_fd, offset, count, headers=(), trailers=(), flags=0)"""
# Скопируйте число байтов из файлового дескриптора in_fd в файловый дескриптор out_fd,
# начиная со смещения. Возвращает количество отправленных байтов. При достижении EOF
# вернуть 0.
# Нотация первой функции поддерживается всеми платформами, определяющими
# функцию sendfile().
# В Linux, если для смещения задано значение None, байты считываются из текущей позиции
# in_fd, а позиция in_fd обновляется.
# Второй случай можно использовать в macOS и FreeBSD, где заголовки и трейлеры
# представляют собой произвольные последовательности буферов, которые записываются до
# и после записи данных из in_fd. Он возвращает то же, что и в первом случае.
# В macOS и FreeBSD значение 0 для count указывает на отправку до тех пор, пока
# не будет достигнут конец in_fd.
# Все платформы поддерживают сокеты в качестве файлового дескриптора out_fd,
# а некоторые платформы допускают и другие типы (например, обычный файл, канал).
# Кроссплатформенные приложения не должны использовать аргументы заголовков,
# трейлеров и флагов.
# Доступность: Unix, не Emscripten, не WASI.
#     Примечание
# Оболочку более высокого уровня для sendfile() см. в разделе socket.socket.sendfile().
#     Новое в версии 3.3.
# Изменено в версии 3.9: Параметры out и in переименованы в out_fd и in_fd.
"""
 os.SF_NODISKIO
 os.SF_MNOWAIT
 os.SF_SYNC
"""
# Параметры функции sendfile(), если реализация их поддерживает.
#      Доступность: Unix, не Emscripten, не WASI.
#      Новое в версии 3.3.
"""
os.SF_NOCACHE
"""
# Параметр функции sendfile(), если реализация поддерживает это. Данные не будут
# кэшироваться в виртуальной памяти и впоследствии будут освобождены.
#      Доступность: Unix, не Emscripten, не WASI.
#      Новое в версии 3.11.

import os

source = './Python_intro.txt'  # Source file path
dest = './newfile.txt'  # destination file path
# Open both files and get the file descriptor using os.open() method
# Откройте оба файла и получите дескриптор файла, используя метод os.open().
src_fd = os.open(source, os.O_RDONLY)
dest_fd = os.open(dest, os.O_RDWR | os.O_CREAT)

# Now send n bytes from source file descriptor to destination file descriptor
# using os.sendfile() method
# Теперь отправьте n байтов из дескриптора исходного файла в дескриптор целевого файла,
# используя метод os.sendfile().
offset = 0
count = 100
bytesSent = os.sendfile(dest_fd, src_fd, offset, count)
print("% d bytes sent / copied successfully." % bytesSent)

# Now read the sent / copied content from destination file descriptor
# Теперь прочитайте отправленный/скопированный контент из дескриптора файла назначения.
os.lseek(dest_fd, 0, 0)
str = os.read(dest_fd, bytesSent)
print(str)   # Print read bytes
# Close the file descriptors
os.close(src_fd)
os.close(dest_fd)
