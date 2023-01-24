"""os.get_inheritable(fd)"""
# Получить «наследуемый» флаг указанного файлового дескриптора (логическое значение).

import os

path = "file.txt"

# Откройте файл и получите связанный с ним файловый дескриптор,
# используя метод os.open().
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# Получить значение наследуемого флага файлового дескриптора fd с помощью метода
# os.get_inheritable()
inheritable = os.get_inheritable(fd)
print("Value of inheritable flag:", inheritable)

# Значение наследуемого флага можно установить/снять с помощью
# метода os.set_inheritable() Например: изменить наследуемый флаг
os.set_inheritable(fd, True)

inheritable = os.get_inheritable(fd)
print("Value of inheritable flag:", inheritable)  # значение наследуемого флага
