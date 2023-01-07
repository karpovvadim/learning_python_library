"""os.truncate(path, length)"""
# Обрезать файл, соответствующий пути, так, чтобы его размер не превышал длины байт.
#      Эта функция может поддерживать указание файлового дескриптора.
#      Вызывает событие аудита os.truncate с аргументами путь, длина.
#      Доступность: Unix, Windows.
#      Новое в версии 3.3.
#      Изменено в версии 3.5: Добавлена поддержка Windows
#      Изменено в версии 3.6: принимает объект, подобный пути.
import os

path = 'test_truncate.txt'
fp = open(path, 'w')
fp.write('truncate data string')
fp = open(path, 'r')
print(fp.read())
fp.close()
os.truncate(path, 8)
fp = open(path, 'r')
print(fp.read())
fp.close()
os.unlink(path)

print('----Using os.truncate() method to truncate a file using a file descriptor----')
path = 'test_fd_truncate.txt'
fd = os.open(path, os.O_RDWR | os.O_CREAT)
s = 'GeeksforGeeks - A Computer Science portal'  # String to be written
line = str.encode(s)  # Convert the string to bytes
os.write(fd, line)
# Ищите файл с самого начала, используя метод os.lseek()
os.lseek(fd, 0, 0)
print(os.read(fd, 50))
os.truncate(fd, 10)
os.lseek(fd, 0, 0)
print(os.read(fd, 15))
os.close(fd)
