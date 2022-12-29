"""os.fstatvfs(fd)"""
# Возвращает информацию о файловой системе, содержащей файл, связанный с файловым
# дескриптором fd, например, statvfs(). Начиная с Python 3.3, это эквивалентно
# os.statvfs(fd).
#       Доступность: Юникс.
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Now get  the touple
info = os.fstatvfs(fd)

print("File Info :", info)

# Now get maximum filename length
print("Maximum filename length :%d" % info.f_namemax)

# Now get free blocks
print("Free blocks :%d" % info.f_bfree)

# Close opened file
os.close(fd)
