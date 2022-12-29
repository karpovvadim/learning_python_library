""" os.fsync(fd)"""
# Принудительная запись файла с файловым дескриптором fd на диск. В Unix это вызывает
# встроенную функцию fsync(); в Windows функция MS _commit().
# Если вы начинаете с буферизованного файлового объекта Python f, сначала выполните
# f.flush(), а затем os.fsync(f.fileno()), чтобы убедиться, что все внутренние буферы,
# связанные с f, записаны на диск.
# Доступность: Unix, Windows.
import os

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, b"This is test")

# Now you can use fsync() method.
# Infact here you would not be able to see its effect.
os.fsync(fd)

# Now read this file from the beginning
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
print("------------------------------------------")
path = 'file_2.txt'

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
# using os.fsync() method
os.fsync(fd)
print("Force write of file committed successfully")

# Close the file descriptor
os.close(fd)
