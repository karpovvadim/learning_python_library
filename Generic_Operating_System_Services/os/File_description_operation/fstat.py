"""os.fstat(fd)"""
# Получить статус файлового дескриптора fd. Возвращает объект stat_result.
# Начиная с Python 3.3, это эквивалентно os.stat(fd).
# See also
# The stat() function.
import os

path = "file_2.txt"

# open the file represented by the above given path and get the file descriptor
# associated with it using os.open() method
# откройте файл, представленный указанным выше путем, и получите связанный с
# ним файловый дескриптор, используя метод os.open()
fd = os.open(path, os.O_RDONLY)

# Get the status of the file descriptor using os.fstat() method
# Получить статус файлового дескриптора с помощью метода os.fstat()
status = os.fstat(fd)
print(status)
os.close(fd)  # close the file descriptor

print("------------------------------------------")
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Now get the touple
info = os.fstat(fd)
print("File Info :", info)
# Now get uid of the file
print("UID of the file :%d" % info.st_uid)
# Now get gid of the file
print("GID of the file :%d" % info.st_gid)
os.close(fd)
