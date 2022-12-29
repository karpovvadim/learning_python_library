#                File Object Creation  (Создание файлового объекта)

# Эти функции создают новые файловые объекты. (См. также open() для
# открытия файловых дескрипторов.)

"""os.fdopen(fd, *args, **kwargs)"""
# Возвращает открытый файловый объект, связанный с файловым дескриптором fd. Это
# псевдоним встроенной функции open() и принимает те же аргументы. Единственное отличие
# состоит в том, что первый аргумент fdopen() всегда должен быть целым числом.
import os

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Now get a file object for the above file. (Теперь получите файловый объект
fo = os.fdopen(fd, "w+")                   # для вышеуказанного файла.)

# Tell the current position   (Сообщите текущую позицию)
print("Current I/O pointer position :%d" % fo.tell())  # Текущая позиция указателя I/O

# Write one string   (Напишите одну строку)
fo.write("Python is a great language.\nYeah its great!!\n")

# Now read this file from the beginning. (Теперь прочитайте этот файл с самого начала.)
os.lseek(fd, 0, 0)
str_ = os.read(fd, 100)
print("Read String is : ", str_)

# Tell the current position   (Сообщите текущую позицию)
print("Current I/O pointer position :%d" % fo.tell())  # Текущая позиция указателя ввода-вывода

# Close opened file (Закрыть открытый файл)
fo.close()
print("Closed the file successfully!!")
