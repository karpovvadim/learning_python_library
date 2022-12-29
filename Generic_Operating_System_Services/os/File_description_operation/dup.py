""" os.dup(fd)"""
# Возвращает дубликат файлового дескриптора fd. Новый файловый дескриптор не подлежит
# наследованию.
# В Windows при дублировании стандартного потока (0: stdin, 1: stdout, 2: stderr)
# наследуется новый файловый дескриптор.
# Наличие: не WASI.
# Изменено в версии 3.4: новый файловый дескриптор теперь не наследуется.
import os

path = "file_2.txt"

# open the file and get the file descriptor associated with it using os.open() method
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# Print the value of file descriptor
print("Original file descriptor:", fd)

# Duplicate the file descriptor
dup_fd = os.dup(fd)

# The duplicated file will have             Дублированный файл будет иметь
# different value but it                    другое значение, но он
# will correspond to the same               будет соответствовать тому же
# file to which original file               файлу, на который ссылался
# descriptor was referring                  исходный файловый дескриптор.

# Print the value of duplicated file descriptor
# Напечатать значение дублированного файлового дескриптора
print("Duplicated file descriptor:", dup_fd)

# Get the list of all file Descriptors Used by the current Process
# (below code works on UNIX systems)
# Получить список всех файловых дескрипторов, используемых текущим процессом
# (приведенный ниже код работает в системах UNIX)
pid = os.getpid()
print("pid:", pid)
os.system("ls -l/proc/%s/fd" % pid)

# Close file descriptors
os.close(fd)
os.close(dup_fd)

print("File descriptor duplicated successfully")
