"""os.get_terminal_size(fd=STDOUT_FILENO)"""
# Возвращает размер окна терминала как (столбцы, строки), кортеж типа terminal_size.
# Необязательный аргумент fd (по умолчанию STDOUT_FILENO или стандартный вывод)
# указывает, какой файловый дескриптор следует запрашивать.
# Если дескриптор файла не подключен к терминалу, возникает ошибка OSError.
# Shutil.get_terminal_size() — это функция высокого уровня, которую обычно следует
# использовать,
# os.get_terminal_size — низкоуровневая реализация.
#      Доступность: Unix, Windows.
import os
# Get the size
# of the terminal
size = os.get_terminal_size()
# Print the size
# of the terminal
print(size)
"""
OSError: [Errno 25] Inappropriate ioctl for device
OSError: [Errno 25] Неподходящий ioctl для устройства
"""
# New in version 3.3.
