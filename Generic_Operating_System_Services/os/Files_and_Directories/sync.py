"""os.sync()"""
# Принудительная запись всего на диск.
#       Доступность: Юникс.
#       Новое в версии 3.3.
import os
path1 = 'file1.txt'
path2 = 'file2.txt'
path3 = 'file3.txt'
fd1 = os.open(path1, os.O_RDWR | os.O_CREAT)
fd2 = os.open(path2, os.O_RDWR | os.O_CREAT)
fd3 = os.open(path3, os.O_RDWR | os.O_CREAT)

str = b"GeeksforGeeks"
os.write(fd1, str)
os.write(fd2, str)
os.write(fd3, str)
# Синхр. все буферы на диск, т.е. принудительно записывать все на диск
# с помощью метода os.sync()
os.sync()
print("Force write everything committed successfully")
os.close(fd1)
os.close(fd2)
os.close(fd3)
# Метод os.sync() сбрасывает все буферы на диск.
# Это может занять значительное время.
