"""os.get_inheritable(fd)"""
# Получить «наследуемый» флаг указанного файлового дескриптора (логическое значение).

import os

path = "file.txt"

# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# Get the value of
# inheritable flag of the
# file descriptor fd using
# os.get_inheritable() method
inheritable = os.get_inheritable(fd)

# print the value of inheritable flag
print("Value of inheritable flag:", inheritable)

# Value of inheritable flag can be set / unset
# using os.set_inheritable() method
# For example:
# change inheritable flag
os.set_inheritable(fd, True)

# Print the value of inheritable flag
inheritable = os.get_inheritable(fd)
print("Value of inheritable flag:", inheritable)
