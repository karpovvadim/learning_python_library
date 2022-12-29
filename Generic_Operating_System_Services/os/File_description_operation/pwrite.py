"""os.pwrite(fd, str, offset)"""
# Запишите строку байтов в str в файловый дескриптор fd по смещению, оставив смещение в
# файле без изменений.
# Возвращает количество фактически записанных байтов.
#      Доступность: Юникс.
#      Новое в версии 3.3.
import os

filename = "file.txt"

fd = os.open(filename, os.O_RDWR)
s = "Python, "           # String to be written in the file (Строка для записи в файл)
text = s.encode("utf-8")     # converting string to bytestring
offset = 5                   # Position from where file writing will start

# As offset is 0, bytestring will be written in the beginning of the file
# Write the bytestring to the file indicated by file descriptor at specified position
# Поскольку смещение равно 0, байтовая строка будет записана в начало файла.
# Запишите строку байтов в файл, указанный файловым дескриптором, в указанной позиции.
bytesWritten = os.pwrite(fd, text, offset)
print("Number of bytes actually written:", bytesWritten)
with open(filename) as f:     # Print the content of the file
    print(f.read())

s = "Javascript, "           # String to be written in the file
text = s.encode("utf-8")     # converting string to bytestring

# Position from where file writing will start os.stat(fd).st_size will return file
# size in bytes so bytestring will be written at the end of the file

# Позиция, с которой начнется запись файла os.stat(fd).st_size вернет размер
# файла в байтах, поэтому строка байтов будет записана в конец файла.
offset = os.stat(fd).st_size

# Write the bytestring to the file indicated by file descriptor at specified position
# Запишите строку байтов в файл, указанный файловым дескриптором, в указанной позиции.
bytesWritten = os.pwrite(fd, text, offset)
print("\nNumber of bytes actually written:", bytesWritten)

with open(filename) as f:
    print(f.read())         # Print the content of the file

s = "R Programming, "       # String to be written in the file
text = s.encode("utf-8")    # converting string to bytestring
offset = 10                 # Position from where file writing will start

# Write the bytestring to the file indicated by file descriptor at specified position
# Запишите строку байтов в файл, указанный файловым дескриптором, в указанной позиции.
bytesWritten = os.pwrite(fd, text, offset)
print("\nNumber of bytes actually written:", bytesWritten)

with open(filename) as f:   # Print the content of the file
    print(f.read())
