"""os.lseek(fd, pos, how)"""
# Установите текущую позицию дескриптора файла fd в позицию pos, измененную как:
# SEEK_SET или 0, чтобы установить позицию относительно начала файла; SEEK_CUR или 1, чтобы
# установить его относительно текущей позиции; SEEK_END или 2, чтобы установить его
# относительно конца файла. Возвращает новую позицию курсора в байтах, начиная с начала.

# pos — это позиция в файле по отношению к заданному параметру как. Вы указываете
# os.SEEK_SET или 0, чтобы установить позицию относительно начала файла,
# os.SEEK_CUR или 1, чтобы установить ее относительно текущей позиции;
# os.SEEK_END или 2, чтобы установить его относительно конца файла.
#
# how — это точка отсчета в файле.
# os.SEEK_SET или 0 означает начало файла,
# os.SEEK_CUR или 1 означает текущую позицию, а
# os.SEEK_END или 2 означает конец файла.
import os

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

os.write(fd, b"This is test")

# Now you can use fsync() method. (Теперь вы можете использовать метод fsync().)
# Infact here you would not be able to see its effect.
# (На самом деле здесь вы не сможете увидеть его эффект.)
os.fsync(fd)

# Now read this file from the beginning
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
