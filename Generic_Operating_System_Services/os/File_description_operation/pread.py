"""os.pread(fd, n, offset)"""
# Прочитать не более n байтов из файлового дескриптора fd по смещению, оставив смещение
# в файле без изменений.
# Возвращает строку байтов, содержащую прочитанные байты. Если достигнут конец файла, на
# который указывает fd, возвращается пустой объект bytes.
#      Доступность: Юникс.
#      Новое в версии 3.3.
import os

# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open("Python_intro.txt", os.O_RDONLY)

# Number of bytes to be read
n = 50

# Read at most n bytes from
# file descriptor fd
# using os.read() method
readBytes = os.read(fd, n)

# Print the bytes read
print(readBytes)

# Now set the Offset value
offset = 1
# Read at most n bytes from
# file descriptor fd at a position of
# given offset value using os.pread() method
readBytes = os.pread(fd, n, offset)

# Print the bytes read
print(readBytes)

# close the file descriptor
os.close(fd)
