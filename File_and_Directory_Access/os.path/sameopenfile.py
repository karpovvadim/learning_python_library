"""os.path.sameopenfile(fp1, fp2)"""
# Верните True, если файловые дескрипторы fp1 и fp2 ссылаются на один и тот же файл.
# Доступность: Unix, Windows.
# Изменено в версии 3.2: Добавлена поддержка Windows.
# Изменено в версии 3.6: принимает объект, подобный пути
import os.path
path = '/home/vadim/python_library/File_and_Directory_Access/os.path/samestat.py'
fd1 = os.open(path, os.O_RDONLY)
fp = open(path, mode ='r')
fd2 = fp.fileno()
print(os.path.sameopenfile(fd1, fd2))
# True

os.close(fd1)
os.close(fd2)
