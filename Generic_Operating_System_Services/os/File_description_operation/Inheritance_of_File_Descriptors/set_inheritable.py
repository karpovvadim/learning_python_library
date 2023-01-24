"""os.set_inheritable(fd, inheritable)"""
# Установите флаг «наследуемый» для указанного файлового дескриптора.
import os
path = "file.txt"
# Откройте файл и получите связанный с ним файловый дескриптор,
# используя метод os.open().
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# Получить текущее значение наследуемого флага дескриптора файла fd,
# используя метод os.get_inheritable().
inheritable_flag = os.get_inheritable(fd)
print("Current value of inheritable flag:", inheritable_flag)

# Измените наследуемый флаг файлового дескриптора fd с помощью
# метода os.set_inheritable().
inheritable = True
os.set_inheritable(fd, inheritable)
print("Inheritable flag modified")

# Распечатайте измененное значение наследуемого флага дескриптора файла,
# используя метод os.get_inheritable().
print("Current value of inheritable flag:", os.get_inheritable(fd))
