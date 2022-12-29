"""os.fdatasync(fd)"""
# Принудительная запись файла с файловым дескриптором fd на диск.
# Не принудительно обновляет метаданные.
#      Доступность: Юникс.
#      Примечание
#      Эта функция недоступна в MacOS.
import os

path = 'file.txt'

# Open the file and get
# the file descriptor
# associated with
# using os.open() method
fd = os.open(path, os.O_RDWR)

# Write a bytestring
str = b"GeeksforGeeks"

os.write(fd, str)


# The written string is
# available in program buffer
# but it might not actually
# written to disk until
# program is closed or
# file descriptor is closed.

# sync. all internal buffers
# associated with the file descriptor
# with disk (force write of file)
# using os.fdatasync() method
os.fdatasync(fd)
print("Force write of file committed successfully")

# Close the file descriptor
os.close(fd)

# os.fdatasync() method
# does not force update of
# metadata. if you want to
# update it too, use
# os.fsync() method instead.
