"""os.ftruncate(fd, length)"""
# Усекает файл, соответствующий файловому дескриптору fd, так, чтобы его размер не
# превышал длины байт. Начиная с Python 3.3, это эквивалентно os.truncate(fd, length).
# Вызывает событие аудита os.truncate с аргументами fd, length.
# Доступность: Unix, Windows.
# Изменено в версии 3.5: Добавлена поддержка Windows

import os

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, b"This is test - This is test")

# Now you can use ftruncate() method.
os.ftruncate(fd, 10)

# Now read this file from the beginning.
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
