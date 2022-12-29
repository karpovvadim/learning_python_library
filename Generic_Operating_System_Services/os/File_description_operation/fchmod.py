"""os.fchmod(fd, mode)"""
# Измените режим файла, заданный fd, на числовой режим. См. документы для chmod() для
# возможных значений режима. Начиная с Python 3.3, это эквивалентно os.chmod(fd, mode).
# Вызывает событие аудита os.chmod с аргументами путь, режим, dir_fd.
# Доступность: Юникс.
# Эта функция ограничена на Emscripten и WASI, см. Платформы WebAssembly для получения
# дополнительной информации.
import os
import stat

filename = "file.txt"

# Open the specified file and get the file descriptor associated with it
# using os.open() method
# Откройте указанный файл и получите связанный с ним файловый дескриптор
# с помощью метода os.open().
fd = os.open(filename, os.O_RDWR)

# Print the current numeric mode (octal notation ) of the file
# Распечатать текущий числовой режим (восьмеричное представление) файла
mode = oct(os.stat(fd).st_mode)[-3:]
print("Current numeric mode of the file (octal notation):", mode)

# Now change the mode of the file
# octal value 777 as mode means read write and execute permission for owner,
# group and others
mode = 0o777
os.fchmod(fd, mode)
print("\nFile mode changed successfully")

# Print the changed numeric mode (octal notation ) of the file
mode = oct(os.stat(fd).st_mode)[-3:]
print("Current numeric mode of the file (octal notation):", mode)

# mode parameter can be also given by flags defined in stat module
# (параметр режима также может быть задан флагами, определенными в модуле stat)
# Change mode
mode = stat.S_IRWXU
os.fchmod(fd, mode)
print("\nFile mode changed successfully")
print("Now, File can be read, write and executed by owner only")

# Print the changed numeric mode
# (octal notation ) of the file
mode = oct(os.stat(fd).st_mode)[-3:]
print("Current numeric mode of the file (octal notation):", mode)

# change mode
mode = stat.S_IRWXU | stat.S_IRGRP
os.fchmod(fd, mode)
print("\nFile mode changed successfully")
print("Now, File can be read, write and executed \
by owner but can be read by group")

# Print the changed numeric mode (octal notation ) of the file
mode = oct(os.stat(fd).st_mode)[-3:]
print("Current numeric mode of the file (octal notation):", mode)

# Close the file descriptor
os.close(fd)
